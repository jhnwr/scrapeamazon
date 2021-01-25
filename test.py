from requests_html import HTMLSession
from my_methods import get_search_urls

# define fn that gets all product_urls from a search_url


dept_url = r'https://www.amazon.com/s?k=medline&i=hpc&rh=n%3A3760901&page='
search_list = get_search_urls(dept_url)
search_list

search_url = search_list[1]


#need to either remove sponsored pages, or scrape seller from the page