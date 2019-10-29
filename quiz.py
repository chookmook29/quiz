from urllib.request import urlopen
import requests
import random
from bs4 import BeautifulSoup



difficulty = 10
playerNumber = random.randint(0, 24)
if difficulty == 1:
	pageNumber = 1
else:
	pageNumber = random.randint(1, difficulty)
title = "Do you know which player is this?"
headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.co.uk/spieler-statistik/wertvollstespieler/marktwertetop?page=" + str(pageNumber)
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
listLinks = []
for a in Players:
    listLinks.append(a['href'])
myPlayer = (listLinks[playerNumber])

page = "https://www.transfermarkt.co.uk" + str(listLinks[playerNumber])
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
clubTeam = pageSoup.find_all("a", {"class": "vereinprofil_tooltip"})
mainPosition = pageSoup.find("div", {"class": "hauptposition-left"})
pastTeam = pageSoup.find_all("a", {"class": "vereinprofil_tooltip"})
value = pageSoup.find("div", {"class": "right-td"})
seasonGames = pageSoup.find("span", {"class": "wert"})
age = pageSoup.find("span", {"class": "dataValue"})
position = (mainPosition.text)
position = position[71:]
ageClean = age.text
ageClean = ageClean[42:44]
dateofB = pageSoup.find_all("a", {"class": "auflistung"})
value_f = value.text
print(value_f.strip())
print(position)
print(clubTeam[0].text)
print(clubTeam[2].text)
print("League games this season: " + seasonGames.text)
print("Age: " + ageClean)
decision = input("Check?")
print(Players[playerNumber].text)

