from requests_html import HTMLSession
from my_methods import get_search_urls

# define fn that gets all product_urls from a search_url


dept_url = r'https://www.amazon.com/s?k=medline&i=hpc&rh=n%3A3760901&page='
search_list = get_search_urls(dept_url)
search_list

search_url = search_list[1]

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


len(prod_url_list)

for url in prod_url:
    print(url)
    

#need to either remove sponsored pages, or scrape seller from the page