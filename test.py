from requests_html import HTMLSession
from my_methods import get_search_urls, get_prod_urls, scrape_info
from time import sleep, time

# define fn that gets all product_urls from a search_url

dept_url = r'https://www.amazon.com/s?k=medline&i=hpc&rh=n%3A3760901&page='
search_list = get_search_urls(dept_url)

prod_info = []
for search_url in search_list[:2]:
    
    prod_urls = get_prod_urls(search_url)
    for prod_url in prod_urls[:2]:
        print('Scraping URL: ', prod_url)
        start_time = time()
        prod_info.append(scrape_info(prod_url))
        exec_time = time() - start_time
        print('Scraping completed in: ', exec_time, ' seconds.')
        sleep(3)

for prod in prod_info:
    print(prod)