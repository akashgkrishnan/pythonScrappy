import requests
from bs4 import BeautifulSoup
from time import sleep

all_quotes = []
base_url = 'http://quotes.toscrape.com/'
url = "/page/1"
print('hi')
while url:
    res = requests.get(base_url+url)
    print(f"now scraping {base_url}{url}")
    soup = BeautifulSoup(res.text,"html.parser")
    quotes = soup.find_all(class_ = "quote")
    i = 0
    for quote in quotes:
        all_quotes.append({
        'text':  quote.find(class_ = "text").get_text(),
        "author":quote.find(class_ = "author").get_text()
        })
        i += 1

    sleep(2)


    next_button = soup.find(class_ = "next")
    url = next_button.find("a")["href"] if next_button else None
print(len(all_quotes))