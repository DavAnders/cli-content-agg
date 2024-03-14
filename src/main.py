import argparse
from src.news_api_client import fetch_top_headlines, fetch_everything
from src.cli_output import display_details, display_summary

def main():
    # argparse object handles command line args, description displayed on help option
    parser = argparse.ArgumentParser(description="Content Aggregator and Analyzer")

    parser.add_argument('--query', type=str, help='Query term for fetching content')
    # parser.add_argument('--lang', type=str, default='en', help='Language of the content (default is English)')
    parser.add_argument('--country', type=str, default='us', help='Country code for articles')
    parser.add_argument('--top', action='store_true', help='Use the top-headlines endpoint')
    args = parser.parse_args()

    if args.top:
        # Ensure country code is provided if using top-headlines
        if not args.country:
            print("Country code is required for top headlines.")
            return
        articles = fetch_top_headlines(args.query, args.country)
    else:
        articles = fetch_everything(args.query)

    display_summary(articles)

    try:
        article_number = int(input("Enter article number for more details, or -1 to exit: ")) - 1
        if 0 <= article_number < len(articles):
            display_details(articles[article_number])
        elif article_number != -1:
            print("Invalid article number.")
    except ValueError:
        print("Please enter a valid number.")
        
if __name__ == "__main__":
    main()
