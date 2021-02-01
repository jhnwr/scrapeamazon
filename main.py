import scraper as s

url_all_depts = r'https://www.amazon.com/s?k=medline'
path_out = r'/Users/ryancheng/Projects/medline_scraper/df_results/df_results.csv'
xpath = r'//*[@id="departments"]/ul'

dept_name_url_pairs = s.get_dept_urls(url_all_depts, xpath)
max_depts, max_pages, max_prods = 1, 1, 2

prod_info = []
for dept_name_url_pair in dept_name_url_pairs[:max_depts]:
    dept_name = dept_name_url_pair[0]
    page_url = dept_name_url_pair[1]
    print('Scraping DEPT: ', dept_name)
    for i in range(max_pages):
        print('Scraping PAGE: ', i)
        prod_urls = s.get_prod_urls(page_url)
        for prod_url in prod_urls[:max_prods]:
            print('Scraping PROD: ', prod_url)
            try:
                prod_info.append(s.scrape_info(prod_url))
            except:
                pass
            # sleep(5)
        page_url = s.get_next_page(page_url)
        if 'medline' not in page_url:
            break

s.prod_info_to_csv(prod_info, path_out)