import httpx
from bs4 import BeautifulSoup

url ='https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts'
headers ={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

def extract_product_data(product):
	try:
		name = product.find('span', class_='productdescriptionbrand').text.strip()
		brand = product.find('span', class_='productdescriptionname').text.strip()
		price = product.find('span', class_='CurrencySizeLarge curprice').text.strip()
		print(f'Name: {name}, Brand: {brand}, Price: {price}')

	except Exception as e:
		print(e)

def main():
	response = httpx.get(url, headers=headers)
	response_html= response.text
	# print(response.text)

	soup= BeautifulSoup(response_html, 'html.parser')
	products = soup.find_all('div', class_='s-productthumbbox')
	for product in products:
		extract_product_data(product)


	# first_product = products[0]

	# import pdb 
	# pdb.set_trace()
	# print(len(products))
	# print(len(soup.find_all('a')))
	# print(len(soup.find_all(class_='frasers-plus-sign-up-link')))




if __name__ == '__main__':
	main()