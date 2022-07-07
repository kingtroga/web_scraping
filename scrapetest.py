from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
else: 
    # Program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement





bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)