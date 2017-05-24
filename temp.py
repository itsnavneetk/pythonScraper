import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def make_soup(url):

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    thepage = response.read()

    '''
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    thepage = urlopen(req).read()
    '''
    #thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


#surl = "https://www.naukri.com/business-intelligence-jobs?xt=catsrch&qf[]=81"
surl = "https://www.naukri.com/microsoft-india-(r&d)-jobs-careers-2265"
#surl = "https://www.naukri.com/microsoft-india-%28r%26d%29-jobs-careers-2265-11"
soup = make_soup(surl)

containers = soup.findAll("a",{"class":"content"})
temp = soup.findAll("div",{"class":"other_details"})
con = containers[0]
t = temp[0]
i = 0

#print(containers[0])

print("\n")
#scrape
p = 1
next1 = "https://www.naukri.com/microsoft-india-%28r%26d%29-jobs-careers-2265-2"
while(next1!=""):

    print("scraping page "+str(p))
    for con in containers:
        t = temp[i]
        '''
        print("container::")
        print(con)

        print("\n other::")
        print(t)
        print("\n")
        '''
        print(".......")
        i = i + 1
    print("final i "+ str(i))
    print("end of page : "+str(p))

    print("scraping from : "+str(next1)+"\n")
    p = p + 1
    print(next1)
    print(p)

    soup = make_soup(next1)
    containers = soup.findAll("a",{"class":"content"})
    temp = soup.findAll("div",{"class":"other_details"})
    next = soup.find("div",{"class":"pagination"})
    con = containers[0]
    t = temp[0]
    i = 0

    next1 = next.findAll("a")
    try:
        next1 = next1[1]['href']
        print("found "+str(next1))
    except:
        print("***** end of the data *****")
        next1 = ""

print("final p "+ str(p))
