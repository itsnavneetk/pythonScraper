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

cat = "Aviation"
#surl = "https://www.naukri.com/business-intelligence-jobs?xt=catsrch&qf[]=81"
#surl = "https://www.naukri.com/information-technology-jobs?qi%5B%5D=25&xt=catsrch"
surl = "https://www.naukri.com/aviation-jobs?xt=catsrch&qi[]=46"
soup = make_soup(surl)


containers = soup.findAll("a",{"class":"content"})
temp = soup.findAll("div",{"class":"other_details"})
con = containers[0]
t = temp[0]
i = 0

#print(containers[0])

p = 1
filename = "nakuri"+cat+".csv"
f = open(filename, "w")
headers = "link, desig, details, org, loc, exp, keyskills, descl, salary \n"
f.write(headers)
next1 = "https://www.naukri.com/aviation-jobs-2"


while(next1!="" and p<=2):
#p for limiting spider

    print("scraping page "+str(p))
    for con in containers:
        print(".......")

        link = con.get('href')
        t = temp[i]
        desig = con.find("li",{"class":"desig"})
        try:
            desig = str(desig.text)
            desig = desig.replace("None","")
        except:
            desig = ""

        details = con.find("ul")
        try:
            details = str(details.text)
            details = details.replace("None","")
        except:
            details = ""

        org = con.find("span",{"class":"org"})
        try:
            org = str(org.text)
            org = org.replace("None","")
        except:
            org = ""

        loc = con.find("span",{"class":"loc"})
        try:
            loc = str(loc.text)
            loc = loc.replace("None","")
        except:
            loc = ""

        exp = con.find("span",{"class":"exp"})
        try:
            exp = str(exp.text)
            exp = exp.replace("None","")
        except:
            exp = ""

        Keyskills = con.find("span",{"class":"skill"})
        try:
            Keyskills = str(Keyskills.text)
            Keyskills = Keyskills.replace("None","")
        except:
            Keyskills = ""

        desc = con.find("span",{"class":"desc"})
        desc1 = str(desc)
        desc1 = desc1.replace("<span class=\"desc\" itemprop=\"description\">","")
        desc1 = desc1.replace("</span>","")
        desc1 = desc1.replace("None","")

        salary = t.find("span",{"class":"salary"})
        salary = str(salary.text)
        salary = salary.strip()
        salary = salary.replace("None","")

        i = i + 1

        f.write(link.replace(",","") + "," + desig.replace(",","")+ "," + details.replace(",","")+","+ org.replace(",","")+","+ loc.replace(",","")+","+ exp.replace(",","")+","+ Keyskills.replace(",","")+","+desc1.replace(",","")+","+ salary.replace(",","")+"\n")
        '''
        print("scraping "+i+" container....")
        print(link+"\n"+desig+"\n"+details+"\n"+org+"\n"+loc+"\n"+exp+"\n"+Keyskills+"\n"+desc1)
        print(salary+"\n")
        '''

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

f.close()
