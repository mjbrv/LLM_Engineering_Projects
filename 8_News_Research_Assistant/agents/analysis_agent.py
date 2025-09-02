from typing import Dict, List
import json
from .base_agent import BaseAgent
import config
from tqdm import tqdm

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("analysis", config.ANALYSIS_AGENT_PROMPT)

    async def process(self, articles: List[Dict]) -> Dict:
        """
        Analyze the content of articles.
        
        Args:
            articles: List of articles to analyze
        Returns:
            Dictionary containing analysis results
        """
        results = {
            'summaries': [],
            'key_points': [],
            'sentiment': [],
            'topics': [],
            'biases': []
        }

        # Create progress bar for article analysis
        with tqdm(total=len(articles), desc="└─ Individual articles", position=2, leave=True) as pbar:
            for article in articles:
                try:
                    analysis = await self._analyze_article(article)
                    results['summaries'].append(analysis['summary'])
                    results['key_points'].extend(analysis['key_points'])
                    results['sentiment'].append(analysis['sentiment'])
                    results['topics'].extend(analysis['topics'])
                    results['biases'].append(analysis['bias'])
                except Exception as e:
                    print(f"\nError analyzing article '{article.get('title', 'Unknown')}': {str(e)}")
                    # Add placeholder results for failed analysis
                    results['summaries'].append("Analysis failed")
                    results['key_points'].append("Analysis failed")
                    results['sentiment'].append({"score": 0, "explanation": "Analysis failed"})
                    results['topics'].append("Unknown")
                    results['biases'].append({"detected": False, "explanation": "Analysis failed"})
                finally:
                    pbar.update(1)

        # Perform overall analysis
        with tqdm(total=1, desc="└─ Overall analysis", position=2, leave=True) as pbar:
            try:
                results['overall_analysis'] = await self._perform_overall_analysis(results)
                pbar.update(1)
            except Exception as e:
                print(f"\nError in overall analysis: {str(e)}")
                results['overall_analysis'] = self._get_default_overall_analysis()
                pbar.update(1)

        return results

    async def _analyze_article(self, article: Dict) -> Dict:
        """Analyze a single article using GPT."""
        analysis_prompt = f"""
        You are an expert content analyst. Analyze the following article carefully and provide insights:

        Title: {article.get('title', '')}
        Content: {article.get('description', '')}
        Source: {article.get('source', {}).get('name', '')}
        
        Return a JSON object with the following structure:
        {{
            "summary": "concise summary of the article",
            "key_points": ["key point 1", "key point 2", "etc"],
            "sentiment": {{
                "score": number_between_negative_1_and_1,
                "explanation": "brief explanation of sentiment"
            }},
            "topics": ["main topic 1", "main topic 2", "etc"],
            "bias": {{
                "detected": true_or_false,
                "explanation": "if bias detected, explain why"
            }}
        }}
        """

        try:
            response = await self._call_openai(
                self._create_messages(analysis_prompt),
                temperature=0.3  # Lower temperature for more consistent JSON
            )
            
            # Use the new parsing method with a default value
            default_analysis = {
                'summary': 'Analysis failed',
                'key_points': ['Analysis failed'],
                'sentiment': {'score': 0, 'explanation': 'Analysis failed'},
                'topics': ['Unknown'],
                'bias': {'detected': False, 'explanation': 'Analysis failed'}
            }
            
            return await self._parse_json_response(response, default_value=default_analysis)
            
        except Exception as e:
            print(f"Error analyzing article '{article.get('title', 'Unknown')}': {str(e)}")
            raise

    async def _perform_overall_analysis(self, results: Dict) -> Dict:
        """Perform overall analysis of all articles."""
        overall_prompt = f"""
        You are an expert news analyst. Analyze this collection of article analyses and provide an overall assessment.
        
        Input data:
        Summaries: {json.dumps(results['summaries'])}
        Key Points: {json.dumps(results['key_points'])}
        Sentiments: {json.dumps(results['sentiment'])}
        Topics: {json.dumps(results['topics'])}
        Biases: {json.dumps(results['biases'])}
        
        Return a JSON object with the following structure:
        {{
            "main_narrative": "overall narrative across articles",
            "common_themes": ["theme 1", "theme 2", "etc"],
            "conflicting_viewpoints": ["viewpoint 1", "viewpoint 2", "etc"],
            "overall_sentiment": "general sentiment across articles",
            "potential_gaps": ["gap 1", "gap 2", "etc"]
        }}
        """

        try:
            response = await self._call_openai(
                self._create_messages(overall_prompt),
                temperature=0.3  # Lower temperature for more consistent JSON
            )
            
            # Use the new parsing method with a default value
            default_analysis = self._get_default_overall_analysis()
            return await self._parse_json_response(response, default_value=default_analysis)
            
        except Exception as e:
            print(f"Error in overall analysis: {str(e)}")
            raise

    def _get_default_overall_analysis(self) -> Dict:
        """Return default overall analysis structure when analysis fails."""
        return {
            'main_narrative': 'Analysis failed',
            'common_themes': [],
            'conflicting_viewpoints': [],
            'overall_sentiment': 'neutral',
            'potential_gaps': ['Analysis failed to complete']
        } 