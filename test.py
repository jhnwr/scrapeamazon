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

url = r'https://www.amazon.com/s?k=medline&rh=n%3A3760901&dc&qid=1611784120&rnid=2941120011&ref=sr_nr_n_1'


flag = True
i = 1
while flag == True and i < 200:
    
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=3)
    url = r.html.next()
    if 'ajax_err' in url:
        flag = False
    print('On page: ', str(i), ' URL: ', url)
    i+=1
    


# ajax_error = 'https://www.amazon.com/gp/prime/ref=nav_prime_ajax_err/146-8293514-4870441'
# 'ajax_err' in ajax_error

# dept_url_base_cleaned = dept_url_base.split('&qid=')[0]
# dept_url_base_cleaned = dept_url_base_cleaned + '&page='
# num_pages = 154
# for i in range(2,num_pages):
#     print(dept_url_base_cleaned + str(i))
    