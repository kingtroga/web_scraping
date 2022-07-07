# Dealing with parents

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')

print(bs.find('img', 
     b{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())