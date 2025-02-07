def hearsay_agent():
    sources = [
        'https://www.reuters.com/finance/cryptocurrencies',
        'https://www.coindesk.com',
        # Add more sources as needed
    ]
    all_articles = []
    for source in sources:
        articles = scrape_news(source)
        filtered_articles = filter_articles(articles)
        all_articles.extend(filtered_articles)

    # Remove duplicates
    seen = set()
    unique_articles = []
    for article in all_articles:
        if article['link'] not in seen:
            unique_articles.append(article)
            seen.add(article['link'])

    return unique_articles