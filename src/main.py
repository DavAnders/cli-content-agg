import argparse

def fetch_content():
    print("fetching content...")

def main():
    # argparse object handles command line args, description displayed on help option
    parser = argparse.ArgumentParser(description="Content Aggregator and Analyzer")
    # fetch flag triggers fetch_content. store true for bool check
    parser.add_argument('--fetch', action='store_true', help='Fetch new content')

    args = parser.parse_args()

    if args.fetch:
        fetch_content()
    
if __name__ == "__main__":
    main()