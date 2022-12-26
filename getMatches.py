from ssl import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

estatisticas_Matches={}
golsMarcados=[]
golsSofridos=[]
adversarios=[]
linkPartidas=[]

def getMatch(clube):
    linkPartidas.clear()
    golsMarcados.clear()
    golsSofridos.clear()
    adversarios.clear()
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
    driver.get("https://www.futebol.com/futebol/inglaterra/equipos/"+clube.replace(" ","-").lower()+"/")
    content = driver.page_source
    soup = BeautifulSoup(content)

    for x in soup.findAll('table', attrs={'class':'table matches table-condensed layout-fixed linked-rows'}):
        getLinks(x)
        for t in x.findAll('tbody',attrs={'class':'open'}): 
            for z in t.findAll('tr',attrs={'class':re.compile(r'event.*')}):
                for y in z.findAll('td',attrs={'class':re.compile(r'^team1')}):
                    for q in z.findAll('td',attrs={'class':re.compile(r'^team2')}):
                        for h in z.findAll('td',attrs={'class':'score'}):
                            for i in h.findAll('a',attrs={'class':'has-score-details'}):
                                time1 = y.find('span')
                                time2 = q.find('span')
                                if time1.text.lower() == clube.lower():
                                    golsFeitos = i.find('span', attrs={'class':'home-score'})
                                    golsTomados = i.find('span', attrs={'class':'away-score'})
                                    adversarios.append(time2.text)
                                    golsMarcados.append(int(re.search(r'\d+',golsFeitos.text)[0])) #Regex para obter somente o número do texto sujo.
                                    golsSofridos.append(int(re.search(r'\d+',golsTomados.text)[0]))
                                else:
                                    golsTomados = i.find('span', attrs={'class':'home-score'})
                                    golsFeitos = i.find('span', attrs={'class':'away-score'})
                                    adversarios.append(time1.text)
                                    golsMarcados.append(int(re.search(r'\d+',golsFeitos.text)[0]))
                                    golsSofridos.append(int(re.search(r'\d+',golsTomados.text)[0]))

    estatisticas_Matches = {clube:{'Gols Marcados':golsMarcados,'Gols Sofridos': golsSofridos},'Adversários':adversarios,'Links':linkPartidas}
   
    return estatisticas_Matches

def getLinks(dados):
    for j in dados.findAll('tbody',attrs={'class':'open'}):
        for z in j.findAll('a',attrs={'class':'has-score-details'}):
            linkPartidas.append(z['href'])