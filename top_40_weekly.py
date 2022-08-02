from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(url).read()
    except HTTPError as e:
        return -1, e
    except URLError as e:
        return 0, e
    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.h1
    except AttributeError as e:
        return None, e
    return title