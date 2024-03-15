# Content Aggregator and Analyzer

This project is a Content Aggregator and Analyzer that fetches news articles using the NewsAPI and analyzes them for sentiment. It also provides the functionality to dump article data into a Go API.

## Setup

### Prerequisites

- Python 3.x
- A NewsAPI API Key ([Get one from NewsAPI](https://newsapi.org/register))
- Go (if running the Go API to store articles)

### Configuration

Before using the CLI tool, you need to create a `config.py` file in the `src` directory with your configuration settings. Here's a template for `config.py`:

```python
# src/config.py

# NewsAPI configuration
news_api = 'your_newsapi_api_key_here'
base_url = 'https://newsapi.org/v2/everything'
top_url = 'https://newsapi.org/v2/top-headlines'

# Go API endpoint
go_api_url = 'http://localhost:8080/articles' # Update with your actual endpoint
