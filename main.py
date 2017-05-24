import urllib
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#myurl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"
myurl = "https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&IsNodeId=1&bop=And&Depa=2125620&PageSize=96&order=BESTMATCH"

#opening up connection, grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
#html parsing

page_soup = soup(page_html, "html.parser")      #make soup

print(page_soup.h1)
#grabs each product

containers = page_soup.findAll("div",{"class":"item-container"})
#print(containers)

#grabbing product names from html

container = containers[0]   #for one listing
#print(container)
#print(container.div.div.a.img["title"])  #print name

#title_container = container.findAll("a",{"class":"item-title"})       a with class item-title
#print(title_container)

#writing in csv

filename = "product.csv"
f = open(filename, "w")

headers = "Brand, Product_name, Price, Shipping \n"
f.write(headers)

#looping through whole html

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    product_price = container.findAll("div",{"class":"item-action"})
    price = product_price[0]
    price1 = price.strong.text
    price2 = price.sup.text
    tPrice = "$"+price1+""+price2

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: "+brand+" Name: "+ product_name + " Price: "+tPrice+" Shipping: "+ shipping + "\n")

    f.write(brand.replace(",","") + "," + product_name.replace(",","")+ "," + tPrice.replace(",","")+","+ shipping+"\n")
f.close()




