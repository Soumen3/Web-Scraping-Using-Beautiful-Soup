from bs4 import BeautifulSoup
import requests


url  = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&p%5B%5D=facets.brand%255B%255D%3DAPPLE&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkFwcGxlIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_6_12.metroExpandable.METRO_EXPANDABLE_Apple_gaming-laptops-store_EDRA19TG8T05_wp3&fm=neo%2Fmerchandising&iid=M_825a0300-771c-497c-9333-db2f9f383179_12.EDRA19TG8T05&ppt=sp&ppn=sp&ssid=oo32t1e7cg0000001716408556992"

response = requests.get(url)
print(response.status_code)


htmlContent = response.content
# print(htmlContent)


soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())


# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find_all('p'))
# print(soup.find(id='omni_script'))

for lilnk in soup.find_all('a'):
	print(lilnk.get('href'))
	

