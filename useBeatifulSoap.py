from bs4 import BeautifulSoup

def extract_product_data(product):
	try:
		name = product.find('span', class_='productdescriptionbrand').text.strip()
		brand = product.find('span', class_='productdescriptionname').text.strip()
		price = product.find('span', class_='CurrencySizeLarge curprice').text.strip()
		print(f'Name: {name}, Brand: {brand}, Price: {price}')

	except Exception as e:
		print(e)


if __name__ == '__main__':
	with open('houseoffraser.html', 'r') as f:
		response_html = f.read()

	soup= BeautifulSoup(response_html, 'html.parser')
	products = soup.find_all('div', class_='s-productthumbbox')
	for product in products:
		extract_product_data(product)