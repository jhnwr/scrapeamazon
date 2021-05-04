from requests_html import HTMLSession
import scraper as s

url_all_depts = r'https://www.amazon.com/s?k=medline'
xpath = r'//*[@id="departments"]/ul/li[9]/span/div/div/ul'
xpath = r'//*[@id="departments"]/ul'

s = HTMLSession()
r = s.get(url_all_depts)
r.html.render(sleep = 3)
node = r.html.xpath(xpath, first = True)


