import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

def make_soup(url):

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    thepage = response.read()


    #thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

cat = "IT_01"
filename = "nakuri"+cat+".csv"

#surl = "https://www.naukri.com/business-intelligence-jobs?xt=catsrch&qf[]=81"
surl = "https://www.naukri.com/it-jobs"
next1 = "https://www.naukri.com/it-jobs-2"       #second page link

soup = make_soup(surl)


containers = soup.findAll("a",{"class":"content"})
temp = soup.findAll("div",{"class":"other_details"})
con = containers[0]
t = temp[0]
i = 0

#print(containers[0])


p = 1



f = open(filename, "w", encoding="utf-8")
headers = "link, desig, details, org, loc, exp, keyskills, descl, salary, date, expLow, expHigh, salLow, salHigh \n"
f.write(headers)


while(next1!="" and p<15):
#p for limiting spider according to number of pages
#date for limiting spider according to date


    print("scraping page "+str(p))
    for con in containers:
        print(".......")

        link = con.get('href')
        link = str(link)
        link = link.replace(",","")

        t = temp[i]
        desig = con.find("li",{"class":"desig"})
        try:
            desig = str(desig.text)
            desig = desig.replace("None"," ")
            desig = desig.replace(",","")

        except:
            desig = ""

        details = con.find("ul")
        try:
            details = str(details.text)
            details = details.replace("None"," ")
            details = details.replace(",","")
        except:
            details = ""

        org = con.find("span",{"class":"org"})
        try:
            org = str(org.text)
            org = org.replace("None"," ")
            org = org.replace(",","")
        except:
            org = ""

        loc = con.find("span",{"class":"loc"})
        try:
            loc = str(loc.text)
            loc = loc.replace("None"," ")
            loc = loc.replace(",","-")
        except:
            loc = ""

        exp = con.find("span",{"class":"exp"})
        expLow =""
        expHigh =""
        try:
            exp = str(exp.text)
            exp = exp.replace("None"," ")
            exp = exp.replace(",","")

            expLow = exp.split("-")[0]
            expHigh = exp.split("-")[1]
            expHigh = expHigh.replace(" yrs","")
        except:
            exp = ""

        Keyskills = con.find("span",{"class":"skill"})
        try:
            Keyskills = str(Keyskills.text)
            Keyskills = Keyskills.replace("None"," ")
            Keyskills = Keyskills.replace(",","-")
        except:
            Keyskills = ""

        desc = con.find("span",{"class":"desc"})
        desc1 = str(desc)
        desc1 = desc1.strip()
        desc1 = desc1.replace("<span class=\"desc\" itemprop=\"description\">","")
        desc1 = desc1.replace("</span>","")
        desc1 = desc1.replace("None"," ")
        desc1 = desc1.replace(",","-")
        desc1 = desc1.replace("&amp;","&")

        salary = t.find("span",{"class":"salary"})
        salary = str(salary.text)
        salary = salary.strip()
        salary = salary.replace("None"," ")
        salary = salary.replace(",","")

        salLow='0'
        salHigh='0'
        if(salary!="Not disclosed"):
            salDigits = re.findall('\d+', salary)
            if(len(salDigits)>0):
                salLow = salDigits[0]+""
            if(len(salDigits)>1):
                salHigh = salDigits[1]+""

        date = t.find("span",{"class":"date"})
        date = str(date.text)
        date = date.strip()
        date = date.replace("None"," ")
        date = date.replace("Few Hours Ago","0")
        date = date.replace("Today","0")
        date = date.replace("Just Now","0")
        date = date.replace(" day ago","")
        date = date.replace(" days ago","")
        date = date.replace(",","")


        days_to_subtract = int(date)

        date = datetime.today() - timedelta(days=days_to_subtract)
        date = str(date.date())

        i = i + 1

        if(link!=""):
            f.write(link + "," + desig+ "," + details+","+ org+","+ loc+","+ exp+","+ Keyskills+","+desc1+","+ salary+","+date+","+ expLow+","+expHigh+","+salLow+","+salHigh+"\n")
        '''
        print("scraping "+i+" container....")
        print(link+"\n"+desig+"\n"+details+"\n"+org+"\n"+loc+"\n"+exp+"\n"+Keyskills+"\n"+desc1)
        print(date)
        print("\n")
        '''
        date = int(days_to_subtract)

    print("final no. of entries "+ str(i))
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

