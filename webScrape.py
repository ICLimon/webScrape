import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Lenovo-Tab-P11-Plus-1st/dp/B09B17DVYR/ref=sr_1_2?qid=1695021332&rnid=16225007011&s=computers-intl-ship&sr=1-2&th=1'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response.status_code)

    # Extract data here
    title_element = soup.find('span', id='productTitle')
    title = title_element.get_text(strip=True) if title_element else 'Title not found'
    print(f'Title: {title}')

    description_element = soup.find('div', id='productDescription')
    description = description_element.get_text() if description_element else 'Description not found'
    print(f'Description: {description}')

    price_element = soup.find('span', class_='a-price-whole')
    price = price_element.get_text(strip=True) if price_element else 'Price not found'
    print(f'Price: {price}')
    
    with open('product_data.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Price', 'Description'])
        writer.writerow([title, price, description])

    print('Data has been saved to product_data.csv')
else:
    print(str(response.status_code)+' - Error loading the page')
  




