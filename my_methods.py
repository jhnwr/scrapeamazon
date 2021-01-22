from requests_html import HTMLSession
import pandas as pd

def get_spec_dict(spec_list):
    spec_dict = {}
    for row in spec_list:
        
        row = row.split('\n')
        key = row[0]
        try:
            val = str(row[1])
        except:
            val = None
        spec_dict[key] = val

    return spec_dict

def get_xpath_list():

    xpath_base = r'//*[@id="product-specification-table"]/tbody/tr[1]'
    xpath_first_half = r'//*[@id="product-specification-table"]/tbody/tr['
    xpath_second_half = r']'

    xpath_list = []
    for i in range(1,20):
        xpath = xpath_first_half + str(i) + xpath_second_half
        xpath_list.append(xpath)
        
    return xpath_list

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    #get product_dict
    product = {}
    product['title'] = r.html.xpath('//*[@id="productTitle"]', first=True).text
    product['price'] = r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    try:
        product['shipping'] = r.html.xpath('//*[@id="price-shipping-message"]/b', first=True).text
    except:
        product['shipping'] = 'unable to get shipping info'
    # get spec_list
    spec_list = []
    xpath_list = get_xpath_list()
    for xpath_item in xpath_list:
        try:
            data = r.html.xpath(xpath_item, first=True).text
            spec_list.append(data)
        except:
            break
    spec_dict = get_spec_dict(spec_list)    
    
    product.update(spec_dict)
    
    return product

def get_product_spec(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    spec_list = []
    xpath_list = get_xpath_list()
    for xpath_item in xpath_list:
        try:
            data = r.html.xpath(xpath_item, first=True).text
            spec_list.append(data)
        except:
            break
    # product['row_1'] = r.html.xpath('//*[@id="product-specification-table"]/tbody/tr[1]', first=True).text

    spec_dict = get_spec_dict(spec_list)
    
    return spec_dict


# //*[@id="product-specification-table"]/tbody/tr[1]/th
