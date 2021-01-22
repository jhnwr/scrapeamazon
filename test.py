def get_prod_spec_xpath_list():

    xpath_base = r'//*[@id="product-specification-table"]/tbody/tr[1]'
    xpath_first_half = r'//*[@id="product-specification-table"]/tbody/tr['
    xpath_second_half = r']'

    xpath_list = []
    for i in range(1,4):
        xpath = xpath_first_half + str(i) + xpath_second_half
        xpath_list.append(xpath)
        
    return xpath_list

get_prod_spec_xpath_list()