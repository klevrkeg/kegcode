import requests
import matplotlib.pyplot as plt
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
from lxml import html
import numpy as np


device_page = 'http://172.16.100.8';

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

page = requests.get(device_page)
tree = html.fromstring(page.content)

soup = BeautifulSoup(urlopen(device_page), "lxml")

data = [];
print(soup.prettify())
count = 0

for br in soup.findAll('br'):
    result = br.nextSibling;
    result[-3:];
   
    data.append (int(result[-3:]));
    count = count+1;
    if count == 59:
        break
    
print(data)

del(data[0])
del(data[0])
print(data)

plt.plot(data)
plt.show()
