import urllib.request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url1 = "https://www.thestar.com.my/news/latest?pgno="
url2 = "#Latest"
url3 = ["{}{}{}".format(url1, str(page), url2) for page in range(1, 10)]
s =[]
for url in url3:
    print(url)
    s.append(url)

for row in s: 
    html = urlopen(row)
    bs = BeautifulSoup(html,"lxml")
    print(bs)