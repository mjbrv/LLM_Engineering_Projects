# News Research Assistant

A multi-agent system that helps research and analyze news articles on any topic. The system uses OpenAI's GPT models and NewsAPI to provide comprehensive news analysis with fact-checking and detailed reporting.

## Features

- 🔍 Smart article search and filtering
- 📊 Deep content analysis
- ✔️ Automated fact-checking
- 📝 Comprehensive report generation
- 🤖 Multiple specialized AI agents working together

## System Architecture

The system consists of four specialized agents:

1. **Search Agent**: Finds and filters relevant news articles
2. **Analysis Agent**: Processes and analyzes article content
3. **Fact-Check Agent**: Verifies information and claims
4. **Report Agent**: Generates comprehensive final reports

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd news-research-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
```

## Usage

Basic usage example:

```python
import asyncio
from news_research_coordinator import NewsResearchCoordinator

async def main():
    coordinator = NewsResearchCoordinator()
    
    # Define your research parameters
    topic = "Artificial Intelligence Ethics"
    time_range = {
        'start': '2024-01-01',
        'end': '2024-03-14'
    }
    
    # Get the research report
    report = await coordinator.research_topic(topic, time_range)
    
    # Access different sections of the report
    print(report['executive_summary'])
    print(report['detailed_analysis'])
    print(report['recommendations'])

if __name__ == "__main__":
    asyncio.run(main())
```

## Report Structure

The final report includes:

- Executive Summary
- Detailed Analysis
  - Topic Analysis
  - Source Analysis
  - Narrative Analysis
  - Fact Check Summary
- Recommendations
- Metadata

## Requirements

- Python 3.8+
- OpenAI API key
- NewsAPI key
- Required Python packages (see requirements.txt)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 