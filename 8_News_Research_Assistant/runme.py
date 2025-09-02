
import asyncio
from news_research_coordinator_light import NewsResearchCoordinatorLight

async def main():
    coordinator = NewsResearchCoordinatorLight()
    
    # Define your research parameters
    topic = "Artificial Intelligence Ethics"
    time_range = {
        'start': '2025-05-17',
        'end': '2025-05-19'
    }
    
    # Get the research report
    report = await coordinator.research_topic(topic, time_range)
    
    # Access different sections of the report
    # print(report['executive_summary'])
    # print(report['detailed_analysis'])
    # print(report['recommendations'])

if __name__ == "__main__":
    asyncio.run(main())