import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerdatasaved = ""
for letter in ascii_lowercase:
    soup = make_soup("http://www.basketball-reference.com/players/"+letter+"/")

    for record in soup.findAll('tr'):
            playerdata = ""
            for name in record.findAll('th'):
                playerdata = playerdata+","+name.text
            for data in record.findAll('td'):
                playerdata = playerdata+","+data.text
            playerdatasaved = playerdatasaved + "\n" + playerdata[1:]
    print(playerdatasaved)


headers = "Player,From,To,Pos,Ht,Wt,Birth Date,College"+"\n"
filename = "player.csv"
f = open(os.path.expanduser(filename), "wb")
f.write(bytes(headers, encoding="ascii", errors='ignore'))
f.write(bytes(playerdatasaved, encoding="ascii", errors='ignore'))


f.close()
