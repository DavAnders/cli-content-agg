# Content Aggregator and Analyzer
**Note**: This project is split into two parts: the Python CLI tool (this repository) and the [Go API](https://github.com/DavAnders/cli-agg-api) for storing and processing articles. Please make sure to also check out the [Go API repository](https://github.com/DavAnders/cli-agg-api) for the complete functionality.

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

## Usage
The CLI tool supports various flags to control its behavior:

- `--query`: Specify the query term for fetching content. Use this to search for specific topics or articles.
- `--country`: (Used with `--top`) Specify the country code for fetching top headlines.
- `--top`: Use this flag to fetch top headlines instead of searching all articles. Requires `--country`.
- `--details`: After fetching articles, use this flag to enter an interactive mode that prompts for more details on individual articles.

### Interaction with Go API

When fetching articles, the CLI tool automatically posts the article data to the specified Go API endpoint (`go_api_url` in `config.py`). Ensure your Go API is running and accessible for this feature to work.

This setup requires the Go API part of the project to be properly configured and running. Please visit [the Go API repository](https://github.com/DavAnders/cli-agg-api) for instructions on setting up and running the Go API.