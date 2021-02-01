import scraper as s

search_term = r'medline'
url_all_depts = r'https://www.amazon.com/s?k=' + search_term
dir_out = r'/Users/ryancheng/Projects/medline_scraper/df_results/'

dept_name_url_pairs = s.get_dept_urls(url_all_depts, xpath = r'//*[@id="departments"]/ul')
# max_depts = 10
max_pages = 1
max_prods = 1

for dept_name_url_pair in dept_name_url_pairs:
    dept_name = dept_name_url_pair[0]
    page_url = dept_name_url_pair[1]
    prod_info = []
    for i in range(1, max_pages + 1):
        try:
            prod_urls = s.get_prod_urls(page_url)
            j = 1
            for prod_url in prod_urls:
                print('Scraping DEPT:', dept_name, '. Page No:', i, '. Prod No:', j)
                try:
                    prod_info.append(s.scrape_info(prod_url))
                except:
                    pass
                j+=1
                if j > max_prods:
                    break
        except:
            pass

        page_url = s.get_next_page(page_url)
        if 'medline' not in page_url:
            break
    path_out = dir_out + search_term + '_' + str(dept_name) + '.csv'
    try:
        s.prod_info_to_csv(prod_info, path_out)
    except:
        pass



