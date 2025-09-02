from typing import Dict, List
import json
from .base_agent import BaseAgent
import config

class ReportAgent(BaseAgent):
    def __init__(self):
        super().__init__("report", config.REPORT_AGENT_PROMPT)

    async def process(self, data: Dict) -> Dict:
        """
        Generate a comprehensive report from the analyzed data.
        
        Args:
            data: Dictionary containing all analysis results
        Returns:
            Formatted report
        """
        try:
            # Generate executive summary
            executive_summary = await self._generate_executive_summary(data)
            
            # Generate detailed sections
            detailed_analysis = await self._generate_detailed_analysis(data)
            
            # Compile final report
            report = {
                'executive_summary': executive_summary,
                'detailed_analysis': detailed_analysis,
                'metadata': {
                    'total_articles': len(data.get('articles', [])),
                    'analysis_timestamp': data.get('timestamp', ''),
                    'topic': data.get('topic', '')
                }
            }

            # Generate recommendations
            report['recommendations'] = await self._generate_recommendations(data, report)

            return report
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            return {
                'executive_summary': {
                    'main_findings': 'Report generation failed',
                    'key_trends': [],
                    'critical_insights': [],
                    'reliability_assessment': ''
                },
                'detailed_analysis': {},
                'metadata': {},
                'recommendations': []
            }

    async def _generate_executive_summary(self, data: Dict) -> Dict:
        """Generate an executive summary of the findings."""
        try:
            analysis = data.get('analysis', {})
            summary_prompt = f"""
            Create an executive summary of the following news analysis:
            
            Topic: {data.get('topic', '')}
            Number of Articles: {len(data.get('articles', []))}
            Overall Analysis: {json.dumps(analysis.get('overall_analysis', {}))}
            Key Findings: {json.dumps(analysis.get('key_points', []))}
            
            Return the summary in JSON format with the following structure:
            {{
                "main_findings": "2-3 sentences on the most important findings",
                "key_trends": ["list", "of", "key", "trends"],
                "critical_insights": ["list", "of", "critical", "insights"],
                "reliability_assessment": "overall assessment of the information reliability"
            }}
            """

            response = await self._call_openai(self._create_messages(summary_prompt))
            
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                print("Error parsing executive summary")
                return {
                    'main_findings': '',
                    'key_trends': [],
                    'critical_insights': [],
                    'reliability_assessment': ''
                }
        except Exception as e:
            print(f"Error generating executive summary: {str(e)}")
            return {
                'main_findings': 'Summary generation failed',
                'key_trends': [],
                'critical_insights': [],
                'reliability_assessment': ''
            }

    async def _generate_detailed_analysis(self, data: Dict) -> Dict:
        """Generate detailed analysis sections."""
        try:
            # Safely get analysis and fact check results
            analysis = data.get('analysis', {})
            fact_check_results = data.get('fact_check_results', [])
            
            # Extract fact check data safely
            verified_claims = []
            unverified_claims = []
            credibility_scores = []
            
            for result in fact_check_results:
                if isinstance(result, dict):
                    verification = result.get('verification_results', {})
                    verified_claims.extend(verification.get('verified_claims', []))
                    unverified_claims.extend(verification.get('unverified_claims', []))
                    cred = verification.get('credibility_assessment', {})
                    if isinstance(cred, dict):
                        credibility_scores.append({
                            'source_credibility': float(cred.get('source_credibility', 0)),
                            'evidence_quality': float(cred.get('evidence_quality', 0)),
                            'overall_reliability': float(cred.get('overall_reliability', 0))
                        })

            analysis_prompt = f"""
            Create a detailed analysis report from the following data:
            
            Analysis Results: {json.dumps(analysis)}
            Verified Claims: {json.dumps(verified_claims)}
            Unverified Claims: {json.dumps(unverified_claims)}
            Credibility Scores: {json.dumps(credibility_scores)}
            
            Return the analysis in JSON format with the following structure:
            {{
                "topic_analysis": {{
                    "main_topics": ["list", "of", "topics"],
                    "topic_relationships": ["how", "topics", "relate"],
                    "emerging_themes": ["list", "of", "themes"]
                }},
                "source_analysis": {{
                    "source_distribution": "analysis of sources used",
                    "credibility_assessment": "overall source credibility",
                    "potential_biases": ["identified", "biases"]
                }},
                "narrative_analysis": {{
                    "main_narratives": ["identified", "narratives"],
                    "competing_viewpoints": ["different", "viewpoints"],
                    "supporting_evidence": ["evidence", "summary"]
                }},
                "fact_check_summary": {{
                    "verified_claims": ["list", "of", "verified", "claims"],
                    "disputed_claims": ["list", "of", "disputed", "claims"],
                    "unverified_claims": ["list", "of", "unverified", "claims"]
                }}
            }}
            """

            response = await self._call_openai(self._create_messages(analysis_prompt))
            
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                print("Error parsing detailed analysis")
                return {
                    'topic_analysis': {},
                    'source_analysis': {},
                    'narrative_analysis': {},
                    'fact_check_summary': {}
                }
        except Exception as e:
            print(f"Error generating detailed analysis: {str(e)}")
            return {
                'topic_analysis': {},
                'source_analysis': {},
                'narrative_analysis': {},
                'fact_check_summary': {}
            }

    async def _generate_recommendations(self, data: Dict, report: Dict) -> List[Dict]:
        """Generate recommendations based on the analysis."""
        try:
            recommendations_prompt = f"""
            Based on the following analysis, generate recommendations for further investigation:
            
            Executive Summary: {json.dumps(report.get('executive_summary', {}))}
            Detailed Analysis: {json.dumps(report.get('detailed_analysis', {}))}
            
            Return recommendations in JSON format as an array of objects with the following structure:
            [{{
                "recommendation": "specific recommendation",
                "rationale": "why this is important",
                "priority": "high/medium/low",
                "suggested_actions": ["specific", "actions", "to", "take"]
            }}]
            """

            response = await self._call_openai(self._create_messages(recommendations_prompt))
            
            try:
                recommendations = json.loads(response)
                if not isinstance(recommendations, list):
                    return []
                return recommendations
            except json.JSONDecodeError:
                print("Error parsing recommendations")
                return []
        except Exception as e:
            print(f"Error generating recommendations: {str(e)}")
            return [] 