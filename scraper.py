from requests_html import HTMLSession
import pandas as pd

# define fn that gets all dept urls from all search
def get_dept_urls(url_all_depts, xpath):
    s = HTMLSession()
    r = s.get(url_all_depts)
    r.html.render(sleep = 1)
    node = r.html.xpath(xpath, first = True)
    lis = node.find('li')
    
    dept_url_list = []
    for li in lis:

        span = li.find('span', first = True)
        a = span.find('a', first = True)
        href = a.attrs['href']
        url_base = r'https://www.amazon.com'
        dept_url = url_base + href
        dept_url_list.append(dept_url)
        
    return dept_url_list


def get_path_delimiter():

    path_delimiter = [
        (r'//*[@id="detailBullets_feature_div"]/ul/li/span', ' : '),
        (r'//*[@id="productDetails_techSpec_section_1"]/tbody/tr', '\n'),
        (r'//*[@id="productDetails_detailBullets_sections1"]/tbody/tr', '\n'),
        (r'//*[@id="product-specification-table"]/tbody/tr', '\n')
    ]
    return path_delimiter

def get_items_from_list(r, xpath, delimiter = '\n'):

    scrape_dict = {}
    nodes = r.html.xpath(xpath)
    for node in nodes:
        try:
            key, val = node.text.split(delimiter)
            scrape_dict[key] = val
        except:
            pass
    return scrape_dict

def scrape_info(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    #get product_dict
    product = {}
    product['url'] = url
    product['title'] = r.html.xpath('//*[@id="productTitle"]', first=True).text
    product['price'] = r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    
    string = r.html.xpath('//*[@id="bylineInfo"]', first = True).text
    string = string.split('Visit the ')[1].split(' Store')[0]
    product['seller'] = string 

    try:
        product['shipping'] = r.html.xpath('//*[@id="price-shipping-message"]/b', first=True).text
    except:
        product['shipping'] = 'unable to get shipping info'
        
    # get items from tables
    path_delimiter = get_path_delimiter()
    for thing in path_delimiter:
        xpath, delimiter = thing
        list_dict = get_items_from_list(r, xpath, delimiter)
        product.update(list_dict)
    
    return product

# define fn that gets number of pages

# define fn that gets all search url pages from dept url
# TODO add funcationality to stop (e.g. page 155 DNE for alot of depts)
# This function actually does not work anymore
def get_search_urls(dept_url, num_pages = 155):

    url_list = []
    for i in range(1,num_pages):
        url = dept_url + str(i)
        url_list.append(url)
        
    return url_list

# define fn that gets all product_urls from a search_url
def get_prod_urls(search_url):

    s = HTMLSession()
    r = s.get(search_url)
    r.html.render(sleep=1)

    xpath = r'//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div'

    deeper_xpath = r'//*[@id="search"]/div[1]/div[2]/div/span[3]/div/div/div/span/div/div/div/div/span/a'
    results_page = r.html.xpath(deeper_xpath)

    prod_url_list = []
    for node in results_page:
        
        url_end = node.attrs['href']
        url_base = r'https://www.amazon.com'
        prod_url = url_base + url_end
        prod_url_list.append(prod_url)


    return prod_url_list

#need to either remove sponsored pages, or scrape seller from the page