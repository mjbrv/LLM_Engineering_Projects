import asyncio
from datetime import datetime
from typing import Dict, List
from agents.search_agent import SearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent
import os
from tqdm import tqdm

class NewsResearchCoordinatorLight:
    def __init__(self):
        # Verify API keys are set
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if not os.getenv("NEWS_API_KEY"):
            raise ValueError("NEWS_API_KEY not found in environment variables")
            
        self.search_agent = SearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.report_agent = ReportAgent()

    def _format_report_markdown(self, report: Dict, topic: str) -> str:
        """Format the report in markdown."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        md_content = f"""# Research Report: {topic}
Generated on: {timestamp}

## Executive Summary
{report['executive_summary']['main_findings']}

## Key Trends
"""
        for trend in report['executive_summary'].get('key_trends', []):
            md_content += f"- {trend}\n"

        md_content += "\n## Critical Insights\n"
        for insight in report['executive_summary'].get('critical_insights', []):
            md_content += f"- {insight}\n"

        md_content += "\n## Reliability Assessment\n"
        md_content += report['executive_summary'].get('reliability_assessment', 'No reliability assessment available.')

        md_content += "\n\n## Detailed Analysis\n"
        detailed = report.get('detailed_analysis', {})
        
        # Topic Analysis
        md_content += "\n### Topic Analysis\n"
        topic_analysis = detailed.get('topic_analysis', {})
        md_content += "\n#### Main Topics\n"
        for topic in topic_analysis.get('main_topics', []):
            md_content += f"- {topic}\n"
        
        md_content += "\n#### Topic Relationships\n"
        for rel in topic_analysis.get('topic_relationships', []):
            md_content += f"- {rel}\n"
        
        md_content += "\n#### Emerging Themes\n"
        for theme in topic_analysis.get('emerging_themes', []):
            md_content += f"- {theme}\n"

        # Source Analysis
        md_content += "\n### Source Analysis\n"
        source_analysis = detailed.get('source_analysis', {})
        md_content += f"\n**Source Distribution**: {source_analysis.get('source_distribution', 'Not available')}\n"
        md_content += f"\n**Credibility Assessment**: {source_analysis.get('credibility_assessment', 'Not available')}\n"
        
        md_content += "\n#### Potential Biases\n"
        for bias in source_analysis.get('potential_biases', []):
            md_content += f"- {bias}\n"

        # Recommendations
        md_content += "\n## Recommendations\n"
        for rec in report.get('recommendations', []):
            md_content += f"\n### {rec['priority']} Priority\n"
            md_content += f"**Recommendation**: {rec['recommendation']}\n\n"
            md_content += f"**Rationale**: {rec['rationale']}\n"

        return md_content

    def _save_report(self, content: str, topic: str) -> str:
        """Save the report to a markdown file."""
        # Create reports directory if it doesn't exist
        os.makedirs('reports', exist_ok=True)
        
        # Format filename: topic_YYYY-MM-DD_HHMMSS.md
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        # Clean topic name for filename (remove special characters)
        clean_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).strip()
        clean_topic = clean_topic.replace(' ', '_')
        
        filename = f"reports/{clean_topic}_{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filename

    async def research_topic(self, topic: str, time_range: Dict[str, str] = None) -> Dict:
        """
        Coordinate the research process across all agents.
        
        Args:
            topic: The topic to research
            time_range: Optional dictionary with 'start' and 'end' dates
        Returns:
            Complete analysis report
        """
        try:
            # Create progress bars for each step
            search_pbar = tqdm(total=1, desc="🔍 Searching for articles", position=0, leave=True)
            analysis_pbar = tqdm(total=1, desc="📊 Analyzing articles", position=1, leave=True)
            report_pbar = tqdm(total=1, desc="📝 Generating final report", position=2, leave=True)

            # Step 1: Search for articles
            articles = await self.search_agent.process({
                'topic': topic,
                'time_range': time_range
            })
            search_pbar.update(1)
            search_pbar.close()

            if not articles:
                analysis_pbar.close()
                report_pbar.close()
                return {
                    'error': 'No articles found',
                    'topic': topic,
                    'timestamp': datetime.now().isoformat(),
                    'executive_summary': {'main_findings': 'No articles found for the given topic'},
                    'detailed_analysis': {},
                    'recommendations': []
                }

            # Step 2: Analyze articles
            analysis_results = await self.analysis_agent.process(articles)
            analysis_pbar.update(1)
            analysis_pbar.close()

            # Step 3: Generate report
            report_data = {
                'topic': topic,
                'timestamp': datetime.now().isoformat(),
                'articles': articles,
                'analysis': analysis_results
            }
            
            final_report = await self.report_agent.process(report_data)
            
            # Format and save the report
            md_content = self._format_report_markdown(final_report, topic)
            report_file = self._save_report(md_content, topic)
            
            report_pbar.update(1)
            report_pbar.close()
            
            print(f"\n✨ Research complete! Report saved to: {report_file}")
            return final_report

        except Exception as e:
            print(f"\nError during research process: {str(e)}")
            return {
                'error': str(e),
                'topic': topic,
                'timestamp': datetime.now().isoformat(),
                'executive_summary': {'main_findings': f'Error occurred: {str(e)}'},
                'detailed_analysis': {},
                'recommendations': []
            }

async def main():
    # Example usage
    coordinator = NewsResearchCoordinatorLight()
    
    # Research a topic
    topic = "Artificial Intelligence Ethics"
    time_range = {
        'start': '2024-01-01',
        'end': '2024-03-14'
    }
    
    report = await coordinator.research_topic(topic, time_range)
    
    if 'error' in report:
        print(f"\n❌ Error: {report['error']}")

if __name__ == "__main__":
    asyncio.run(main()) 