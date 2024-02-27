import requests
import sys
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Columbia-Mens-wind-\ 
resistant-Glove/dp/B0772WVHPS/?_encoding=UTF8&pd_rd\ 
_w=d9RS9&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf\ 
_rd_r=7MP3ZDYBBV88PYJ7KEMJ&pd_rd_r=550bec4d-5268-41d5-\ 
87cb-8af40554a01e&pd_rd_wg=oy8v8&ref_=pd_gw_cr_cartx&th=1"
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

  




