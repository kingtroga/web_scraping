# Dealing with siblings

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(child)