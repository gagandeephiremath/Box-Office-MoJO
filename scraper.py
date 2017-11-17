import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

rows = []
url = 'http://www.boxofficemojo.com/yearly/chart/?page=%d&view=releasedate&view2=domestic&yr=2016&p=.htm'
url_list =[]
def urls():
	for page in range(1,9):
#page = 1
		full_url = url%page
		url_list.append(full_url)
	return url_list
urls()
def soups(x):
	for i in x:
		response = requests.get(i)
		page = response.content
		soup = BeautifulSoup(page, "lxml")
#print(soup)
		tables = soup.find('table', attrs={'cellpadding':'5'})
		for i in tables.find_all("tr")[2:103]:
			cells = []
			for cell in i.find_all("td")[1:]:
				text = cell.text
				cells.append(text)
			rows.append(cells)

	with open("output.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(rows)
df = pd.read_csv('output.csv')
df.columns=['title','studio','gross','theaters','opengross','opentheaters','open','close']
df.to_csv('data.csv', index=False)
soups(url_list)
print(rows)

