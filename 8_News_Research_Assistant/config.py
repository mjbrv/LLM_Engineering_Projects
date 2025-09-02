import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Agent Roles and Prompts
SEARCH_AGENT_PROMPT = """You are a Search Agent specialized in finding and filtering news articles.
Your task is to:
1. Evaluate the relevance of articles to the given topic
2. Filter out low-quality or irrelevant content
3. Ensure diverse source selection
4. Rank articles by importance and credibility"""

ANALYSIS_AGENT_PROMPT = """You are an Analysis Agent specialized in processing news content.
Your tasks include:
1. Summarizing article content
2. Extracting key points and insights
3. Analyzing sentiment and tone
4. Identifying main topics and themes
5. Detecting potential biases"""

FACT_CHECK_AGENT_PROMPT = """You are a Fact-Checking Agent specialized in verification.
Your tasks include:
1. Cross-referencing facts across multiple sources
2. Evaluating source credibility
3. Identifying potential misinformation
4. Verifying claims against trusted sources"""

REPORT_AGENT_PROMPT = """You are a Report Generation Agent specialized in creating comprehensive news summaries.
Your tasks include:
1. Organizing information in a clear structure
2. Highlighting key findings and insights
3. Creating executive summaries
4. Identifying trends and patterns
4. Formatting information for easy consumption"""

# System Configuration
MAX_ARTICLES_PER_SEARCH = 10
TEMPERATURE_SETTINGS = {
    "search": 0.3,
    "analysis": 0.4,
    "fact_check": 0.2,
    "report": 0.5
}

# Output Configuration
REPORT_SECTIONS = [
    "executive_summary",
    "key_findings",
    "detailed_analysis",
    "fact_check_results",
    "sources_and_citations"
] 