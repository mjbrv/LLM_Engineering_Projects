from typing import Dict, List
import json
from .base_agent import BaseAgent
import config
import asyncio
from datetime import datetime
import aiohttp
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from tqdm import tqdm

class FactCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("fact_check", config.FACT_CHECK_AGENT_PROMPT)
        self.max_concurrent = 3  # Maximum number of concurrent API calls

    async def process(self, articles: List[Dict]) -> List[Dict]:
        """
        Verify facts from the articles.
        
        Args:
            articles: List of articles to fact check
        Returns:
            List of fact-checking results
        """
        # Create semaphore for rate limiting
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        # Create tasks for parallel processing
        with tqdm(total=len(articles), desc="└─ Verifying claims", position=3, leave=True) as pbar:
            async def process_article(article: Dict) -> Dict:
                async with semaphore:  # Rate limit API calls
                    try:
                        verification = await self._verify_article(article)
                        pbar.update(1)
                        return {
                            'article_url': article.get('url', ''),
                            'verification_results': verification,
                            'article_data': article  # Keep the original article data
                        }
                    except Exception as e:
                        print(f"\nError fact-checking article '{article.get('title', 'Unknown')}': {str(e)}")
                        pbar.update(1)
                        return {
                            'article_url': article.get('url', ''),
                            'verification_results': self._get_default_verification(),
                            'article_data': article  # Keep the original article data
                        }
            
            # Process all articles in parallel
            fact_check_results = await asyncio.gather(
                *[process_article(article) for article in articles]
            )

        return fact_check_results

    async def _verify_article(self, article: Dict) -> Dict:
        """Verify an article's claims in a single API call."""
        verification_prompt = f"""
        You are an expert fact-checker. Analyze the following article and verify its claims:

        Title: {article.get('title', '')}
        Content: {article.get('description', '')}
        Source: {article.get('source', {}).get('name', 'Unknown Source')}
        URL: {article.get('url', '')}
        
        Return a JSON object with the following structure:
        {{
            "verified_claims": [
                {{
                    "claim": "specific claim from the article",
                    "verification_status": "confirmed/partially_confirmed/unconfirmed/false",
                    "evidence": "supporting or contradicting evidence",
                    "confidence": "high/medium/low"
                }}
            ],
            "unverified_claims": [
                {{
                    "claim": "claim that couldn't be verified",
                    "reason": "why verification wasn't possible"
                }}
            ],
            "credibility_assessment": {{
                "source_credibility": "score between 0 and 1",
                "evidence_quality": "score between 0 and 1",
                "overall_reliability": "score between 0 and 1"
            }},
            "verification_summary": "brief summary of the fact-checking results"
        }}
        
        Focus on factual claims that can be verified through reliable sources.
        """

        try:
            response = await self._call_openai(
                self._create_messages(verification_prompt),
                temperature=0.2  # Lower temperature for more conservative fact-checking
            )
            
            parsed_response = await self._parse_json_response(
                response,
                default_value=self._get_default_verification()
            )
            
            # Ensure all fields are present with proper types
            verification_result = {
                'verified_claims': [],
                'unverified_claims': [],
                'credibility_assessment': {
                    'source_credibility': 0.0,
                    'evidence_quality': 0.0,
                    'overall_reliability': 0.0
                },
                'verification_summary': ''
            }
            
            # Safely copy data from parsed response
            if isinstance(parsed_response.get('verified_claims'), list):
                verification_result['verified_claims'] = parsed_response['verified_claims']
            if isinstance(parsed_response.get('unverified_claims'), list):
                verification_result['unverified_claims'] = parsed_response['unverified_claims']
            if isinstance(parsed_response.get('credibility_assessment'), dict):
                cred = parsed_response['credibility_assessment']
                verification_result['credibility_assessment'] = {
                    'source_credibility': float(cred.get('source_credibility', 0)),
                    'evidence_quality': float(cred.get('evidence_quality', 0)),
                    'overall_reliability': float(cred.get('overall_reliability', 0))
                }
            verification_result['verification_summary'] = str(parsed_response.get('verification_summary', ''))
            
            return verification_result
            
        except Exception as e:
            print(f"\nError in verification: {str(e)}")
            return self._get_default_verification()

    def _get_default_verification(self) -> Dict:
        """Return default verification structure when verification fails."""
        return {
            'verified_claims': [],
            'unverified_claims': [],
            'credibility_assessment': {
                'source_credibility': 0.0,
                'evidence_quality': 0.0,
                'overall_reliability': 0.0
            },
            'verification_summary': 'Verification failed'
        }

    async def _cross_reference_claim(self, claim: str) -> List[str]:
        """Cross-reference a claim with multiple sources."""
        # This would typically involve web searches or accessing fact-checking databases
        # For demo purposes, we'll use a simplified version
        async with aiohttp.ClientSession() as session:
            # Here you could add actual API calls to fact-checking services
            # For now, we'll return a placeholder
            return [
                "Would integrate with fact-checking APIs",
                "Could use multiple news sources for verification",
                "Might include academic databases for specific claims"
            ] 