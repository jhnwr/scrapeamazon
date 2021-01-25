from my_methods import getPrice, get_product_spec
import pandas as pd

# TODO create method to get a url list
# This will also need to be a slow cralwer so as not to get detected

url1 = r'https://www.amazon.com/Medline-Washable-Underpads-Incontinence-Training/dp/B07P83ZDV4'
url2 = r'https://www.amazon.com/FitRight-Diapers-Disposable-Incontinence-Absorbency/dp/B00KHUMB1E'
url3 = r'https://www.amazon.com/FitRight-Heavyweight-Cleansing-Unscented-Incontinence/dp/B01KGH1T92'

url_list = [url1, url2, url3]

product_info_list = []

for url in url_list:
    product_info = getPrice(url)
    product_info_list.append(product_info)

df_list = []
for product in product_info_list:
    
    df = pd.DataFrame(product, index=[0])
    df_list.append(df)
    
df = pd.concat(df_list)

path_out = r'/Users/ryancheng/Projects/scrapeamazon/df_results.csv'

df.to_csv(path_out)

len(product_info_list)

