import argparse
from src.news_api_client import fetch_top_headlines, fetch_everything, post_article_to_db
from src.cli_output import display_details, display_summary

def main():
    # argparse object handles command line args, description displayed on help option
    parser = argparse.ArgumentParser(description="Content Aggregator and Analyzer")

    parser.add_argument('--query', type=str, help='Query term for fetching content')
    parser.add_argument('--country', type=str, default='us', help='Country code for articles, used with --top')
    parser.add_argument('--top', action='store_true', help='Use the top-headlines endpoint')
    parser.add_argument('--details', action='store_true', help='Prompt for more details after summary')
    args = parser.parse_args()

    if args.top:
        # Ensure country code is provided if using top-headlines
        if not args.country:
            print("Country code is required for top headlines.")
            return
        articles = fetch_top_headlines(args.query, args.country)
        for article in articles:
            post_article_to_db(article)
    else:
        articles = fetch_everything(args.query)
        for article in articles:
            post_article_to_db(article)

    display_summary(articles)

    if args.details:
        while True:
            try:
                article_number = int(input("Enter article number for more details, or -1 to exit: ")) - 1
                if article_number == -2:
                    break  # User chose to exit
                if 0 <= article_number < len(articles):
                    display_details(articles[article_number])
                else:
                    print("Invalid article number.")
            except ValueError:
                print("Please enter a valid number.")
        
if __name__ == "__main__":
    main()
