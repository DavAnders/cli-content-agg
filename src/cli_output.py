def display_summary(articles):
    print("Displaying summary for fetched articles...")
    for i, article in enumerate(articles):
        print(f"{i+1}. {article['title']} (Polarity: {article['polarity']:.2f} Subjectivity: {article['subjectivity']:.2f} Date: {article['publishedAt'][:10]})")

def display_details(article):
    print(f"Title: {article['title']}")
    print(f"Date: {article['publishedAt']}")
    print(f"URL: {article['url']}")
    print(f"Content: {article['content'][:3000]}")
    