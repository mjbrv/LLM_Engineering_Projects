from typing import Dict, List
import json
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from .base_agent import BaseAgent
import config
from tqdm import tqdm

class SearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("search", config.SEARCH_AGENT_PROMPT)
        self.news_api = NewsApiClient(api_key=config.NEWS_API_KEY)

    async def process(self, query: Dict[str, str]) -> List[Dict]:
        """
        Process the search query and return relevant articles.
        
        Args:
            query: Dict containing 'topic' and optional 'time_range'
        Returns:
            List of filtered and ranked articles
        """
        # Get raw articles from NewsAPI
        raw_articles = await self._fetch_articles(query)
        
        if not raw_articles:
            tqdm.write("No articles found from NewsAPI")
            return []
        
        # Why using "tqdm.write" instead of "print()"?
        # To ensure the "Found articles" message not interupting the progress bar's visual 
        tqdm.write(f"Found {len(raw_articles)} articles from NewsAPI")
        
        # Use GPT to evaluate and rank articles
        ranked_articles = await self._rank_articles(raw_articles, query['topic'])
        
        return ranked_articles[:config.MAX_ARTICLES_PER_SEARCH]

    async def _fetch_articles(self, query: Dict[str, str]) -> List[Dict]:
        """Fetch articles from NewsAPI."""
        try:
            # Calculate date range
            end_date = datetime.now()
            start_date = end_date - timedelta(days=7)  # Default to last 7 days
            if 'time_range' in query:
                start_date = datetime.fromisoformat(query['time_range']['start'])
                end_date = datetime.fromisoformat(query['time_range']['end'])

            response = self.news_api.get_everything(
                q=query['topic'],
                from_param=start_date.isoformat(),
                to=end_date.isoformat(),
                language='en',
                sort_by='relevancy'
            )
            
            # Ensure all required fields are present with defaults
            articles = []
            for article in response['articles']:
                processed_article = {
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'url': article.get('url', ''),
                    'source': {'name': article.get('source', {}).get('name', 'Unknown Source')},
                    'publishedAt': article.get('publishedAt', ''),
                    'content': article.get('content', '')
                }
                articles.append(processed_article)
            
            return articles
            
        except Exception as e:
            print(f"Error fetching articles: {e}")
            return []

    async def _rank_articles(self, articles: List[Dict], topic: str) -> List[Dict]:
        """Use GPT to evaluate and rank articles."""
        if not articles:
            return []

        # Prepare articles for GPT evaluation
        articles_for_evaluation = []
        for idx, article in enumerate(articles):
            try:
                articles_for_evaluation.append({
                    'id': idx,
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'source': article.get('source', {}).get('name', 'Unknown Source'),
                    'url': article.get('url', ''),
                    'publishedAt': article.get('publishedAt', '')
                })
            except Exception as e:
                print(f"Error processing article {idx} for evaluation: {str(e)}")
                continue

        if not articles_for_evaluation:
            return articles[:config.MAX_ARTICLES_PER_SEARCH]

        # Create prompt for GPT
        evaluation_prompt = f"""
        You are an expert news curator. Evaluate and rank the following articles based on their relevance to the topic: '{topic}'
        
        Evaluation criteria:
        1. Relevance to the topic
        2. Source credibility
        3. Information quality
        4. Timeliness
        
        Articles to evaluate:
        {json.dumps(articles_for_evaluation, indent=2)}
        
        Return a JSON object with the following structure:
        {{
            "ranked_articles": [
                {{
                    "id": "article id number",
                    "relevance_score": "score between 0 and 1",
                    "explanation": "brief explanation of why this article is relevant"
                }}
            ]
        }}
        
        Include ONLY the most relevant articles, ranked by importance.
        """

        try:
            # Get GPT's evaluation
            response = await self._call_openai(
                self._create_messages(evaluation_prompt),
                temperature=0.3  # Lower temperature for more consistent JSON
            )
            
            # Parse the response using the new method
            parsed_response = await self._parse_json_response(
                response,
                default_value={"ranked_articles": []}
            )
            
            # Match ranked articles with original articles
            ranked_articles = []
            for ranked in parsed_response.get('ranked_articles', []):
                try:
                    article_id = int(ranked['id'])
                    if article_id < len(articles):
                        article = articles[article_id].copy()
                        article['relevance_score'] = float(ranked.get('relevance_score', 0))
                        article['ranking_explanation'] = ranked.get('explanation', '')
                        ranked_articles.append(article)
                except (ValueError, KeyError, IndexError) as e:
                    print(f"Error processing ranked article: {str(e)}")
                    continue
            
            if not ranked_articles:
                return articles[:config.MAX_ARTICLES_PER_SEARCH]
            
            # Sort by relevance score
            ranked_articles.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
            return ranked_articles
            
        except Exception as e:
            print(f"Error in ranking articles: {str(e)}")
            # Fall back to original articles if parsing fails
            return articles[:config.MAX_ARTICLES_PER_SEARCH] 