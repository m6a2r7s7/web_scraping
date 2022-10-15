import requests
import bs4
from fake_headers import Headers
from pprint import pprint

HEADERS = Headers(browser="chrome",
                  os="win",
                  headers=True).generate()

base_url = "https://habr.com"
url = base_url + "/ru/all/"

KEYWORDS = ['дизайн', 'SEO', 'web', 'python']

response = requests.get(url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")

result = []

articles = soup.find_all("article")
for article in articles:
    names = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    data = [name.text.strip() for name in names]
    for d in data:
        for word in KEYWORDS:
            if word in d:
                dates = article.find_all(class_="tm-article-snippet__datetime-published")
                dates = [date.text.strip() for date in dates]
                data.extend(dates)
                href = article.find(class_="tm-article-snippet__readmore").attrs["href"]
                link = base_url + href
                data.append(link)
                result.append(data)
            else:
                None

pprint(result)
