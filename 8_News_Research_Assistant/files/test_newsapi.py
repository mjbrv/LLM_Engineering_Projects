from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

def test_newsapi():
    # Load environment variables
    load_dotenv()
    
    # Get API key from environment
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print("❌ Error: NEWS_API_KEY not found in .env file")
        return
    
    try:
        # Initialize NewsAPI client
        newsapi = NewsApiClient(api_key=api_key)
        
        # Test API with a simple query
        response = newsapi.get_everything(
            q='technology',
            language='en',
            page_size=1
        )
        
        if response and response['status'] == 'ok':
            print("✅ NewsAPI connection successful!")
            print("\nSample article:")
            article = response['articles'][0]
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Published: {article['publishedAt']}")
        else:
            print("❌ Error: Unexpected response from NewsAPI")
            
    except Exception as e:
        print(f"❌ Error connecting to NewsAPI: {str(e)}")

if __name__ == "__main__":
    test_newsapi() 