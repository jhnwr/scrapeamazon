from requests_html import HTMLSession
from my_methods import get_search_urls, get_prod_urls, scrape_info, get_items_from_list
from time import sleep, time
import pandas as pd
# TODO create method to get a url list
# This will also need to be a slow cralwer so as not to get detected

url1 = r'https://www.amazon.com/Medline-Remedy-Unscented-Olivamine-Repair/dp/B008107QBM/ref=sr_1_8?dchild=1&keywords=medline&qid=1611687162&s=hpc&sr=1-8&th=1'
url2 = r'https://www.amazon.com/Medline-Remedy-Phytoplex-Nourishing-Cream/dp/B00C0LPCZ0/ref=psdc_11060681_t1_B008107QBM'
url_spec_box = r'https://www.amazon.com/Medline-Disposable-incontinence-Furniture-Protection/dp/B075HKJZ2R/ref=sr_1_2?dchild=1&keywords=medline&qid=1611690950&s=hpc&sr=1-2'
prod = scrape_info(url_spec_box)

path_out = r'/Users/ryancheng/Projects/scrapeamazon/df_results_TEST.csv'

df = pd.DataFrame(prod, index = [0])
df.to_csv(path_out)