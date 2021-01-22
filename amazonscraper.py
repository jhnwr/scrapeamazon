from my_methods import getPrice, get_product_spec

url1 = r'https://www.amazon.com/Medline-Washable-Underpads-Incontinence-Training/dp/B07P83ZDV4'
url2 = r'https://www.amazon.com/FitRight-Diapers-Disposable-Incontinence-Absorbency/dp/B00KHUMB1E'
url3 = r'https://www.amazon.com/FitRight-Heavyweight-Cleansing-Unscented-Incontinence/dp/B01KGH1T92'

# url_list = [url1, url2, url3]
# url_list = [url1]
spec_list = []

product = get_product_spec(url1)

product_list = [product]

