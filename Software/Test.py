import csv
import requests
from bs4 import BeautifulSoup 

url='http://www.dublincity.ie/dublintraffic/carparks.htm'
response = requests.get(url)
html= response.content

soup=BeautifulSoup(html)
table=soup.find('tbody', attrs={'id' :'itemsBody'})

list_of_rows=[]
for row in table.findAll('tr'):
	list_of_cells=[]
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;','')
		list_of_cells.append(text)
	list_of_cells.append(list_of_cells)

outfile= open("./carpark.csv", "wb")
writer=csv.writer(outfile)
writer.writerows(["location","spaces"])
writer.writerows(list_of_rows)