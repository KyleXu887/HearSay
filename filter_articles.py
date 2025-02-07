def filter_articles(articles):
    filtered = []
    for article in articles:
        content = article['title'] + " " + article['summary']
        if any(keyword.lower() in content.lower() for keyword in keywords):
            filtered.append(article)
    return filtered