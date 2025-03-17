import requests
from bs4 import BeautifulSoup

def fetch_news(company):
    query = f"{company} news"
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for item in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
        title = item.get_text()
        link = item.find_parent('a')['href']
        articles.append({"title": title, "link": link})
    
    return articles[:10]  # Return top 10 articles

if __name__ == "__main__":
    print(fetch_news("Tesla"))
