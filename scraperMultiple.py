import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

def make_soup(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    thepage = response.read()
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

#surl = "https://www.tripadvisor.in/Hotel_Review-g737163-d4829716-Reviews-Hotel_Green_Park_Suites_Manipal-Manipal_Udupi_District_Karnataka.html"
surl = "https://www.tripadvisor.in/Hotel_Review-g60763-d224223-Reviews-Nyma_the_New_York_Manhattan_Hotel-New_York_City_New_York.html#REVIEWS"
soup = make_soup(surl)
link = soup.find(attrs={"class":"nav next rndBtn ui_button primary taLnk"})
#print(link.get('href'))
nextLink = "https://www.tripadvisor.in"+link.get('href')
i = 2
print("page: 1 ** "+nextLink)

while(nextLink!=""):
    i = str(i)
    print("page: "+i+" ** "+nextLink)
    i = int(i)
    i = i+1
    soup = make_soup(nextLink)
    link = soup.find(attrs={"class":"nav next rndBtn ui_button primary taLnk"})
    print(link.get('href'))
    nextLink = "https://www.tripadvisor.in"+link.get('href')


print("spider")
