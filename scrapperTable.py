import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerdatasaved = ""
soup = make_soup("http://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):
    playerdata = ""
    for name in record.findAll('th'):
        playerdata = playerdata+","+name.text
    for data in record.findAll('td'):
        playerdata = playerdata+","+data.text
    playerdatasaved = playerdatasaved + "\n" + playerdata[1:]
print(playerdatasaved)



filename = "player.csv"
f = open(filename, "w")

headers = "Player,From,To,Pos,Ht,Wt,Birth Date,College \n"
f.write(headers)
f.write(playerdatasaved, encoding = "ascii", errors='ignore')
f.close()
