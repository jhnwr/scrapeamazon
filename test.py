from requests_html import HTMLSession
import scraper as s
import pandas as pd

page_url = r'https://www.amazon.com/s?k=medline&rh=n%3A3760901&dc&qid=1611784120&rnid=2941120011&ref=sr_nr_n_1'
page_url = r'https://www.amazon.com/s?k=medline&i=hpc&rh=n%3A3760901&dc&page=111&qid=1611961390&rnid=2941120011&ref=sr_pg_111'

url_all_depts = r'https://www.amazon.com/s?k=medline'
xpath = r'//*[@id="departments"]/ul'

name_url_pair = s.get_dept_urls(url_all_depts, xpath)

for i, j in range(1,100), range(101, 200):
    print(i,j)