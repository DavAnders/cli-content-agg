# Command Line News Content Aggregator and Analyzer
**Note**: This project is split into two parts: the Python CLI tool (this repository) and the [Go API](https://github.com/DavAnders/cli-agg-api) for storing and processing articles. Please make sure to also check out the [Go API repository](https://github.com/DavAnders/cli-agg-api) for the complete functionality.

This project fetches news articles from NewsAPI and displays the subjectivity and polarity of the content. It also provides the functionality to dump article data into a Go API.

## Why?
There are a lot of news sources, and a lot of opinions. With this tool, you get to sidestep the tedium of manual searches and dive straight into understanding the vibe of the articles through sentiment analysis. Further insight into trends or other data manipulation can be done once an API is setup to receive the data.

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
go_api_url = 'http://localhost:8080/articles'
```
## Usage
The CLI tool supports various flags to control its behavior:

- `--query`: Specify the query term for fetching content. Use this to search for specific topics or articles.
- `--country`: (Used with `--top`) Specify the country code for fetching top headlines.
- `--top`: Use this flag to fetch top headlines instead of searching all articles. Requires `--country`.
- `--details`: After fetching articles, use this flag to enter an interactive mode that prompts for more details on individual articles.

### Interaction with Go API

When fetching articles, the CLI tool automatically posts the article data to the specified Go API endpoint (`go_api_url` in `config.py`). Ensure your Go API is running and accessible for this feature to work.

This setup requires the Go API part of the project to be properly configured and running. Please visit [the Go API repository](https://github.com/DavAnders/cli-agg-api) for instructions on setting up and running the Go API.

## 🤝 Contributing

### Clone the repo

```bash
git clone https://github.com/DavAnders/cli-content-agg
cd cli-content-agg
```

### Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install dependencies

```bash
pip install -r requirements.txt
```

### Configuration

```bash
news_api = 'your_api_key_here'
base_url = 'https://newsapi.org/v2/everything'
top_url = 'https://newsapi.org/v2/top-headlines'
go_api_url = 'http://localhost:8080/articles'
```

### Run the project

```bash
python -m src.main --query "your interest"
```
or for details:

```bash
python main.py --query "something_cool" --details
```
or for top headlines:

```bash
python main.py --top --country us --query "breaking_news"
```

### Run the tests

```bash
python -m unittest FILEPATH
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
