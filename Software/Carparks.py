from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.dublincity.ie/dublintraffic/carparks.htm'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"id":"itemsDiv"})

filename = "Carparks.csv"
f = open(filename, "w")


headers = "location, location_name, space\n"

f.write("headers")

for container in containers:
	location = container.tbody.tr["td"]

	title_container = container.findAll("td", {"class":"locations"})
	location_name = title_container[0].text

	space_container = container.findAll("td",{"class":"spaces"})
	space = space_container[0].text.strip()

	print("location: " + location)
	print("location_name: " + location_name)
	print("space: " + space)

	f.write(location + "," + location_name.replace("," , "|") + "," + space + "\n")

f.close()