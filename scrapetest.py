# understanding findAll() and find()
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')


# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

# Code to find all the number of times "the price" is surrounded by tags
# on the example page
nameList = bs.findAll(text='the prince')
print(len(nameList))