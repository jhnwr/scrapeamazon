from requests_html import HTMLSession
import scraper as s
from time import sleep, time
import pandas as pd
# TODO create method to get a url list
# This will also need to be a slow cralwer so as not to get detected

# def fn that gets number of pages in dept
# grab the text of the num pages
# go to that page - 1
# grab text of num pages
# got to that page -1
# continue until text is not present

page_url = r'https://www.amazon.com/s?k=medline&rh=n%3A3760901&dc&qid=1611784120&rnid=2941120011&ref=sr_nr_n_1'
page_url = r'https://www.amazon.com/s?k=medline&i=hpc&rh=n%3A3760901&dc&page=111&qid=1611961390&rnid=2941120011&ref=sr_pg_111'

for i in range(200):
    
    s = HTMLSession()
    r = s.get(page_url)
    r.html.render(sleep=3)
    page_url = r.html.next()

    print('On page: ', str(i), ' URL: ', page_url)    
    if 'medline' not in page_url:
        break

def get_next_page(page_url):
    s = HTMLSession()
    r = s.get(page_url)
    r.html.render(sleep=5)
    page_url = r.html.next()
    return page_url
