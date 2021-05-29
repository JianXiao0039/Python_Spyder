from urllib.request import *
from bs4 import BeautifulSoup
try:
    html = urlopen("https://www.cnblogs.com/3cH0-Nu1L")
except HTTPErrorProcessor as a:
    print(a)
else:
    if html is None:
        print("URL is not FOund")
    else:
        bsObj = BeautifulSoup(html.read(), "lxml")

print(bsObj.body.h1)