from requests_html import HTMLSession
import scraper as s
from time import sleep, time
import pandas as pd
start_time = time()

# define fn that gets all product_urls from a search_url

# dept_url = r'https://www.amazon.com/s?k=medline&i=hpc&rh=n%3A3760901&page='

url_all_depts = r'https://www.amazon.com/s?k=medline'
xpath = r'//*[@id="departments"]/ul'
dept_urls = s.get_dept_urls(url_all_depts)

dept_url = dept_urls[0]

search_list = s.get_search_urls(dept_url)

prod_info = []
for search_url in search_list[:1]:
    
    prod_urls = s.get_prod_urls(search_url)
    for prod_url in prod_urls:
        print('Scraping URL: ', prod_url)
        try:
            prod_info.append(s.scrape_info(prod_url))
        except:
            pass
        sleep(5)

i = 0
df_list = []
for prod in prod_info:
    df = pd.DataFrame(prod, index = [i])
    df_list.append(df)
    i+=1
    
df = pd.concat(df_list)

path_out = r'/Users/ryancheng/Projects/scrapeamazon/df_results.csv'

df.to_csv(path_out)

exec_time = time() - start_time
print('Scraping completed in: ', exec_time, ' seconds.')
