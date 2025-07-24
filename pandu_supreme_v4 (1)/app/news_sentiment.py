import httpx
from app.config import CRYPTOPANIC_API_KEY

def fetch_cryptopanic():
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={CRYPTOPANIC_API_KEY}&filter=important"
    r = httpx.get(url)
    news = []
    if r.status_code == 200 and 'results' in r.json():
        for item in r.json()['results']:
            news.append({'title': item['title'], 'url': item['url'], 'time': item['created_at']})
    return news
