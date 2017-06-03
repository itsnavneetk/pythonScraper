import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

def make_soup(url):

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    thepage = response.read()


    #thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

cat = "HR"
filename = "nakurit"+cat+".csv"

#surl = "https://www.naukri.com/business-intelligence-jobs?xt=catsrch&qf[]=81"
surl = "https://www.naukri.com/hr-jobs"
next1 = "https://www.naukri.com/hr-jobs-2"       #second page link

soup = make_soup(surl)


containers = soup.findAll("a",{"class":"content"})
temp = soup.findAll("div",{"class":"other_details"})
con = containers[0]
t = temp[0]
i = 0

#print(containers[0])


f = open(filename,'r')
pData = f.read()
f.close()
firstR = ""
with open(filename, newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    firstR = row
    break

firstR = str(firstR)
parts = firstR.split(",")

f.close()
#check for overwriting end

p = 1



f = open(filename, "w", encoding="utf-8")
headers = "uID, link, desig, details, org, loc, exp, keyskills, descl, salary, date \n"
f.write(headers)


while(next1!="" and p<7):
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
            loc = loc.replace(",","")
        except:
            loc = ""

        exp = con.find("span",{"class":"exp"})
        try:
            exp = str(exp.text)
            exp = exp.replace("None"," ")
            exp = exp.replace(",","")
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
        desc1 = desc1.replace("<span class=\"desc\" itemprop=\"description\">","")
        desc1 = desc1.replace("</span>","")
        desc1 = desc1.replace("None"," ")
        desc1 = desc1.replace(",","-")

        salary = t.find("span",{"class":"salary"})
        salary = str(salary.text)
        salary = salary.strip()
        salary = salary.replace("None"," ")
        salary = salary.replace(",","")

        date = t.find("span",{"class":"date"})
        date = str(date.text)
        date = date.strip()
        date = date.replace("None"," ")
        date = date.replace("Few Hours Ago","0 day ago")
        date = date.replace("Today","0 day ago")
        date = date.replace("Just Now","0 day ago")
        date = date.replace(" day ago","")
        date = date.replace(" days ago","")
        date = date.replace(",","")


        if desig in parts[1] and details in parts[2] and org in parts[3] and Keyskills in parts[6] and desc1 in parts[7] and salary in parts[8] :
            print("***stale data***")
            p = 100
            break
        else:
            print("fresh data")
            i = i + 1
            f.write(link + "," + desig+ "," + details+","+ org+","+ loc+","+ exp+","+ Keyskills+","+desc1+","+ salary+","+date+"\n")
            '''
            print("scraping "+i+" container....")
            print(link+"\n"+desig+"\n"+details+"\n"+org+"\n"+loc+"\n"+exp+"\n"+Keyskills+"\n"+desc1)
            print(date)
            print("\n")
            '''
            date = int(date)

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

f.write(pData)
f.close()

