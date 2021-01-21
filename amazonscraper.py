from requests_html import HTMLSession
import pandas as pd

url = 'https://www.amazon.com/Cardinal-Moderate-Absorbency-Protective-Underwear/dp/B076X4GRPT/ref=sr_1_1_sspa?dchild=1&keywords=cardinal+health&qid=1611254997&sr=8-1-spons&psc=1&smid=AE309QMZ3IOFX&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzN0pUVzFQQ0c2RkJTJmVuY3J5cHRlZElkPUEwMDM5MzEzTTlKTk9PV1NLNUpGJmVuY3J5cHRlZEFkSWQ9QTA5MzgxODcxME0wNFdLM1BST08xJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,
            'shipping': r.html.xpath('//*[@id="price-shipping-message"]/b', first = True).text,
            'quantity': r.html.xpath('//*[@id="variation_item_package_quantity"]/div/span', first = True).text
        }
        print(product)
    except:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': 'item unavailable'
        }
        print(product)
    return product

getPrice(url)

tvprices = []
for url in urls:
    tvprices.append(getPrice(url))

print(len(tvprices))

pricesdf = pd.DataFrame(tvprices)
pricesdf.to_excel('tvprices.xlsx', index=False)

