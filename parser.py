import csv
import random
import requests
from bs4 import BeautifulSoup


with open('trmtrkt.csv', mode='w') as csv_file:
    page_mechanism = 1
    trmtrkt_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    trmtrkt_writer.writerow(['name', 'nat_team', 'position', 'value', 'club', 'age', 'games'])
    while page_mechanism < 21:
        playerNumber = 0
        while playerNumber < 25:
            headers = {'User-Agent': 
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            page = "https://www.transfermarkt.co.uk/spieler-statistik/wertvollstespieler/marktwertetop?page=" + str(page_mechanism)
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
            age = pageSoup.find("span", {"class": "dataValue"})
            ageClean = age.text
            ageClean = ageClean[40:44]
            ageClean = ageClean.replace(' ', '')
            ageClean = ageClean.replace(')', '')
            ageClean = ageClean.replace('(', '')
            mainPosition = pageSoup.find("div", {"class": "hauptposition-left"})
            if mainPosition is None:
                mainPosition = pageSoup.find("div", {"class": "hauptposition-center"})
            position = (mainPosition.text)
            position = position[71:]
            position = position.strip().lower()
            value = pageSoup.find("div", {"class": "right-td"})
            if value is None:
                value = pageSoup.find("div", {"class": "dataMarktwert"})
                print("No currency!!!!!!!!!")
            value_f = value.text
            seasonGames = pageSoup.find("span", {"class": "wert"})
            if seasonGames is None:
                seasonGames = 0
            else:
                seasonGames = seasonGames.text 
            print(Players[playerNumber].text)
            trmtrkt_writer.writerow([(Players[playerNumber].text), (clubTeam[2].text), position, value_f, (clubTeam[0].text), ageClean, seasonGames])
            playerNumber += 1
        playerNumber = 0
        page_mechanism += 1
