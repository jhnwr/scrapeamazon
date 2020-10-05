from requests_html import HTMLSession

urls = ['https://www.amazon.co.uk/Samsung-TU7100-Smart-CARBON-SILVER/dp/B086WGXQFZ/ref=sr_1_2?dchild=1&keywords=tv&qid=1601927782&refinements=p_n_size_browse-bin%3A9591881031&rnid=161398031&s=home-theater&sr=1-2',
          'https://www.amazon.co.uk/Samsung-TU7100-HDR-Smart-Tizen/dp/B086T39T5D/ref=sr_1_3?dchild=1&keywords=tv&qid=1601927782&refinements=p_n_size_browse-bin%3A9591881031&rnid=161398031&s=home-theater&sr=1-3',
          'https://www.amazon.co.uk/LG-75UN81006LB-Freeview-Freesat-built/dp/B0853M2XB1/ref=sr_1_7?dchild=1&keywords=tv&qid=1601927782&refinements=p_n_size_browse-bin%3A9591881031&rnid=161398031&s=home-theater&sr=1-7']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }
    print(product)
    return product

tvprices = []
for url in urls:
    tvprices.append(getPrice(url))

print(len(tvprices))
