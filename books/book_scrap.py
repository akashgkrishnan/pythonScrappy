import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = "http://books.toscrape.com/catalogue/"
url = "page-1.html"
while url:
    print(f"Scrapping {url.split('.')[-2]}")
    response = requests.get(base_url+url)
    soup = BeautifulSoup(response.text, features="html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        title = book.find("h3").find("a")['title']
        price = book.find(class_ = "product_price").find(class_ = "price_color").get_text()
        all_books.append({
            'title': title,'price': price.replace('Â£', "")})
    next_button = soup.find(class_ = "next")
    url = next_button.find("a")["href"] if next_button else None

    

print("Done Scrapping")



