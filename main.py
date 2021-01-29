from requests_html import HTMLSession
import scraper as s
from time import sleep, time
import pandas as pd
start_time = time()
url_all_depts = r'https://www.amazon.com/s?k=medline'
xpath = r'//*[@id="departments"]/ul'
dept_urls = s.get_dept_urls(url_all_depts, xpath)
max_depts, max_pages, max_prods = 1 , 1, 1
prod_info = []
for dept_url in dept_urls[:max_depts]:
    print('Scraping DEPT: ', dept_url)
    page_url = dept_url
    for i in range(max_pages):
        print('Scraping PAGE: ', page_url)
        prod_urls = s.get_prod_urls(page_url)
        for prod_url in prod_urls[:max_prods]:
            print('Scraping PROD: ', prod_url)
            try:
                prod_info.append(s.scrape_info(prod_url))
            except:
                pass
            sleep(5)
        page_url = s.get_next_page(page_url)
        if 'medline' not in page_url:
            break

i = 0
df_list = []
for prod in prod_info:
    df = pd.DataFrame(prod, index = [i])
    df_list.append(df)
    i+=1
df = pd.concat(df_list)

path_out = r'/Users/ryancheng/Projects/medline_scraper/df_results.csv'
df.to_csv(path_out)

exec_time = time() - start_time
print('Scraping completed in: ', exec_time, ' seconds.')
