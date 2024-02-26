import requests
import sys
from bs4 import BeautifulSoup

URL = str(sys.argv[1])
webPage = requests.get(URL)


soup = BeautifulSoup(webPage.content, 'html.parser')

print(soup)






