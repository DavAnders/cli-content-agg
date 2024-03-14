import requests
from textblob import TextBlob
from config import news_api, top_url, base_url
    
def fetch_everything(query):
    params = {
        'q': query,
        'apiKey': news_api,
        'language': 'en',
    }
    response = requests.get(base_url, params=params)
    articles_data = []

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for article in articles:
            title = article.get('title', 'No title available')
            content = article.get('content', 'Content not available')
            url = article.get('url', 'URL not available')
            published_at = article.get('publishedAt', 'Publication date not available')
            description = article.get('description', 'No description available')

            analysis_text = content if content else title # prefer sentiment analysis on content
            analysis = TextBlob(analysis_text)
            sentiment = analysis.sentiment

            articles_data.append({
                'title': title,
                'description': description,
                'content': content,
                'url': url,
                'publishedAt': published_at,
                'polarity': sentiment.polarity,
                'subjectivity': sentiment.subjectivity,
            })
    else:
        print(f"Failed to fetch articles. Status code: {response.status_code}")
    return articles_data
    

def fetch_top_headlines(query, country='us'):
    params = {
        'q': query,
        'apiKey': news_api,
        'country': country,
    }
    response = requests.get(top_url, params=params)
    country_data = []
    print(f"Request URL: {response.url}")

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for article in articles:
            title = article.get('title', '')
            content = article.get('content', 'Content not available')
            url = article.get('url', 'URL not available')
            published_at = article.get('publishedAt', 'Date not available')

            analysis_text = content if content else title
            analysis = TextBlob(analysis_text)
            sentiment = analysis.sentiment

            country_data.append({
                'title': title,
                'content': content,
                'url': url,
                'publishedAt': published_at,
                'country': country,
                'polarity': sentiment.polarity,
                'subjectivity': sentiment.subjectivity,
            })
        print(f"Returning {len(country_data)} articles in country_data.")
    else:
        print(f"Failed to fetch articles. Status code: {response.status_code}")
    return country_data
