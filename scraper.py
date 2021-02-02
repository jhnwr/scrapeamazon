from requests_html import HTMLSession
import pandas as pd

# define fn that gets all dept urls from all search

sleep = 3

def get_next_page(page_url):
    s = HTMLSession()
    r = s.get(page_url)
    r.html.render(sleep=sleep)
    page_url = r.html.next()
    return page_url

def get_dept_urls(url_all_depts, xpath):

    s = HTMLSession()
    r = s.get(url_all_depts)
    r.html.render(sleep = sleep)
    node = r.html.xpath(xpath, first = True)

    lis = node.find('li')
    dept_url_list = []
    for li in lis:

        span = li.find('span', first = True)
        a = span.find('a', first = True)
        href = a.attrs['href']
        url_base = r'https://www.amazon.com'
        dept_url = url_base + href
        dept_name = li.text
        dept_name = ''.join(e for e in dept_name if e.isalnum())
        name_url_pair = (dept_name, dept_url)
        dept_url_list.append(name_url_pair)
        
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
    r.html.render(sleep=sleep)
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

# define fn that gets all product_urls from a search_url
def get_prod_urls(search_url):

    s = HTMLSession()
    r = s.get(search_url)
    r.html.render(sleep=sleep)

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

def prod_info_to_csv(prod_info, path_out):
    i = 0
    df_list = []
    for prod in prod_info:
        df = pd.DataFrame(prod, index = [i])
        df_list.append(df)
        i+=1

    df = pd.concat(df_list)
    df.to_csv(path_out)

def main():

    search_term = r'medline'
    url_all_depts = r'https://www.amazon.com/s?k=' + search_term
    dir_out = r'/Users/ryancheng/Projects/medline_scraper/df_results/'

    dept_name_url_pairs = s.get_dept_urls(url_all_depts, xpath = r'//*[@id="departments"]/ul')
    # max_depts = 10
    max_pages = 1
    max_prods = 1

    for dept_name_url_pair in dept_name_url_pairs:
        dept_name = dept_name_url_pair[0]
        page_url = dept_name_url_pair[1]
        prod_info = []
        for i in range(1, max_pages + 1):
            try:
                prod_urls = s.get_prod_urls(page_url)
                j = 1
                for prod_url in prod_urls:
                    print('Scraping DEPT:', dept_name, '. Page No:', i, '. Prod No:', j)
                    try:
                        prod_info.append(s.scrape_info(prod_url))
                    except:
                        pass
                    j+=1
                    if j > max_prods:
                        break
            except:
                pass

            page_url = s.get_next_page(page_url)
            if 'medline' not in page_url:
                break
        path_out = dir_out + search_term + '_' + str(dept_name) + '.csv'
        try:
            s.prod_info_to_csv(prod_info, path_out)
        except:
            pass



