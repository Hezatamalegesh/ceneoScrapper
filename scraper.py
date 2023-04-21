import requests
from bs4 import BeautifulSoup

product_code = input("Podaj kod produktu: ")
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if respons.status_code == requests.codes.ok:
    soup = BeautifulSoup(respons.text, 'html.parser')
    opinions = soup.select("div.js_product-review")
    if len(opinions) > 0:
        opinions_all = []
        for opinion in opinions:
            single_opinion = {
                "opinion_id": ,
                "author": ,
                "recommendation": ,
                "stars": ,
                "purchased": ,
                "opinion_date": ,
                "purchase_date": ,
                "useful_count": ,
                "useless_count": ,
                "content": ,
                "pros": ,
                "cons":
        }
    else:
        print("Nie ma opinii")