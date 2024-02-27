import requests
import sys
from bs4 import BeautifulSoup

URL = str(sys.argv[1])
webPage = requests.get(URL)


soup = BeautifulSoup(webPage.content, 'html.parser')

print(soup)

def product(soup)
  data_str = ""
  productInfo = []
   for item in soup.find_all("ul", class_="a-unorderedlist a-nostyle\a-vertical a-spacing-none detail-bullet-list"):
     data_str = data_str + item.get_text() 
     productInfo.append(data_str.split("\n")) 
      data_str = ""
  return productInfo

productResult = product(soup)
for item in pro_result: 
    for j in item: 
        if j is "": 
            pass
        else: 
            print(j)

  




