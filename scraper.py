import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    # This is a placeholder; the actual implementation depends on the website's structure
    for item in soup.find_all('div', class_='article'):
        title = item.find('h2').get_text()
        link = item.find('a')['href']
        summary = item.find('p').get_text()
        articles.append({'title': title, 'link': link, 'summary': summary})

    return articles