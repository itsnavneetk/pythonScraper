import urllib
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



myurl = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

psoup = soup(page_html, 'html.parser')
seven_day = psoup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())  #print html

location = psoup.findAll("h2",{"class":"panel-title"})
location = location[0]
print("location : "+location.text.replace("(SFOC1)",""))

temp = psoup.find("p",{"class":"myforecast-current-sm"})
print("current temperature : "+temp.text)

condition = psoup.find(id="current_conditions_detail")
condition = condition.table.text
print(condition.strip())

forecast = psoup.find(id="seven-day-forecast-body")
forecast = psoup.findAll("div",{"class":"tombstone-container"})
fore = forecast[0]

for fore in forecast:
    print(fore.p.text+" : "+fore.img["alt"])
    short = fore.find("p",{"class":"short-desc"})
    print(short.text)
    shortTemp = fore.find("p",{"class":"temp temp-high"})
    shortLTemp = fore.find("p",{"class":"temp temp-low"})
    if(shortTemp):
        print(shortTemp.text+"\n")
    if(shortLTemp):
        print(shortLTemp.text+"\n")


#forecast = forecast.findAll("p")

'''

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)
#Tonight
#Mostly Clear
#Low: 49 °F


img = tonight.find("img")
desc = img['title']

print(desc)
#Tonight: Mostly clear, with a low around 49. West northwest wind 12 to 17 mph decreasing to 6 to 11 mph after midnight. Winds could gust as high as 23 mph.

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods


['Tonight',
 'Thursday',
 'ThursdayNight',
 'Friday',
 'FridayNight',
 'Saturday',
 'SaturdayNight',
 'Sunday',
 'SundayNight']

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)


['Mostly Clear', 'Sunny', 'Mostly Clear', 'Sunny', 'Slight ChanceRain', 'Rain Likely', 'Rain Likely', 'Rain Likely', 'Chance Rain']
['Low: 49 °F', 'High: 63 °F', 'Low: 50 °F', 'High: 67 °F', 'Low: 57 °F', 'High: 64 °F', 'Low: 57 °F', 'High: 64 °F', 'Low: 55 °F']
['Tonight: Mostly clear, with a low around 49. West northwest wind 12 to 17 mph decreasing to 6 to 11 mph after midnight. Winds could gust as high as 23 mph. ', 'Thursday: Sunny, with a high near 63. North wind 3 to 5 mph. ', 'Thursday Night: Mostly clear, with a low around 50. Light and variable wind becoming east southeast 5 to 8 mph after midnight. ', 'Friday: Sunny, with a high near 67. Southeast wind around 9 mph. ', 'Friday Night: A 20 percent chance of rain after 11pm.  Partly cloudy, with a low around 57. South southeast wind 13 to 15 mph, with gusts as high as 20 mph.  New precipitation amounts of less than a tenth of an inch possible. ', 'Saturday: Rain likely.  Cloudy, with a high near 64. Chance of precipitation is 70%. New precipitation amounts between a quarter and half of an inch possible. ', 'Saturday Night: Rain likely.  Cloudy, with a low around 57. Chance of precipitation is 60%.', 'Sunday: Rain likely.  Cloudy, with a high near 64.', 'Sunday Night: A chance of rain.  Mostly cloudy, with a low around 55.']
'''
