from requests_html import HTMLSession
import pandas as pd

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    product = {}
    product['title'] = r.html.xpath('//*[@id="productTitle"]', first=True).text
    product['price'] = r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    product['shipping'] = r.html.xpath('//*[@id="price-shipping-message"]/b', first=True).text
    product['brand_name'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[1]/td', first = True).text
    product['ean'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[2]/td', first=True).text
    product['included_componenets'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[3]/td', first=True).text
    product['model_number'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[4]/td', first=True).text
    product['num_items'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[5]/td', first=True).text
    product['part_num'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[6]/td', first=True).text
    product['upc'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[10]/td', first=True).text
    # product[''] = r.html.xpath('', first=True).text
    
    print(product)
    return product

url = 'https://www.amazon.com/Medline-Washable-Underpads-Incontinence-Training/dp/B07P83ZDV4?ref_=ast_sto_dp'

getPrice(url)