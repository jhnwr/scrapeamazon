from my_methods import getPrice, get_product_spec

# TODO create method to get a url list
# This will also need to be a slow cralwer so as not to get detected

url1 = r'https://www.amazon.com/Medline-Washable-Underpads-Incontinence-Training/dp/B07P83ZDV4'
url2 = r'https://www.amazon.com/FitRight-Diapers-Disposable-Incontinence-Absorbency/dp/B00KHUMB1E'
url3 = r'https://www.amazon.com/FitRight-Heavyweight-Cleansing-Unscented-Incontinence/dp/B01KGH1T92'

url_list = [url1, url2, url3]

spec_dict_list = []

for url in url_list:
    spec_dict = get_product_spec(url)
    spec_dict_list.append(spec_dict)

for gosh in spec_dict_list:
    print(gosh)