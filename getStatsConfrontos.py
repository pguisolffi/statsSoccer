from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from getMatches import getMatch

atributoNameCasaHome={}
atributoNameVisitanteHome={}
dictInformacoesHome = {}
atributoNameCasaAway={}
atributoNameVisitanteAway={}
dictInformacoesAway = {}
qtdeGolsEmCasa = []
qtdeGolsFora = []
QtdeGolsPrimeiroTempoCasa = []
QtdeGolsPrimeiroTempoFora = []

def getStatsPartidaHome(listaLinks,timeHome,barraProgresso):
    x = 0
    qtdeLinks = len(listaLinks)
    for x in range(qtdeLinks):

        #Atualizar o ProgressBar
        valorCadaIndiceProgresso = 100/qtdeLinks
        barraProgresso['value']=valorCadaIndiceProgresso*(x+1)
        barraProgresso.update()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options) #Para definir em qua navegador irá executar
        
        try:
            driver.get("https://www.futebol.com"+listaLinks[x])

            content = driver.page_source
            soup = BeautifulSoup(content)

            for a in soup.findAll('table', attrs={'class':'table table-condensed'}):
                timeDaCasa = getTimePrincipal(soup)
                for b in a.findAll('tbody'):
                    for c in b.findAll('tr'):
                        qtde_Casa=c.find('td', attrs={'class':'home number'})
                        qtde_Fora=c.find('td', attrs={'class':'away number'})
                        for d in c.findAll('td', attrs={'class':'statistic'}):
                            name=d.find('div', attrs={'class':'statistic-label'})
                            if name:
                                getGolsCasaFora(soup)
                                getGolsTime(soup)
                                try:
                                    if atributoNameCasaHome[name.text]:
                                        if timeDaCasa.lower() == timeHome.lower():
                                            atributoNameCasaHome[name.text].append(qtde_Casa.text)
                                            atributoNameVisitanteHome[name.text].append(qtde_Fora.text)
                                            atributoNameVisitanteHome[name.text].append(qtde_Fora.text)
                                        else:
                                            atributoNameCasaHome[name.text].append(qtde_Fora.text)
                                            atributoNameVisitanteHome[name.text].append(qtde_Casa.text)
                                except:
                                    if timeDaCasa.lower() == timeHome.lower():
                                        atributoNameCasaHome[name.text]=[qtde_Casa.text]
                                        atributoNameVisitanteHome[name.text]=[qtde_Fora.text]    
                                    else:
                                        atributoNameCasaHome[name.text]=[qtde_Fora.text]
                                        atributoNameVisitanteHome[name.text]=[qtde_Casa.text]     

            dictInformacoesHome = {'timeCasa':{'itens':atributoNameCasaHome},'timeVisitante':{'itens':atributoNameVisitanteHome}}
        except:
            continue


    return dictInformacoesHome

def getStatsPartidaAway(listaLinks,timeAway,barraProgresso):
    x = 0
    qtdeLinks = len(listaLinks)
    for x in range(qtdeLinks):

        #Atualizar o ProgressBar
        valorCadaIndiceProgresso = 100/qtdeLinks
        barraProgresso['value']=valorCadaIndiceProgresso*(x+1)
        barraProgresso.update()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options) #Para definir em qua navegador irá executar
        
        try:
            driver.get("https://www.futebol.com"+listaLinks[x])

            content = driver.page_source
            soup = BeautifulSoup(content)

            for a in soup.findAll('table', attrs={'class':'table table-condensed'}):
                timeDaCasa = getTimePrincipal(soup)
                for b in a.findAll('tbody'):
                    for c in b.findAll('tr'):
                        qtde_Casa=c.find('td', attrs={'class':'home number'})
                        qtde_Fora=c.find('td', attrs={'class':'away number'})
                        for d in c.findAll('td', attrs={'class':'statistic'}):
                            name=d.find('div', attrs={'class':'statistic-label'})
                            if name:
                                try:
                                    if atributoNameCasaAway[name.text]:
                                        if timeDaCasa.lower() == timeAway.lower():
                                            atributoNameCasaAway[name.text].append(qtde_Casa.text)
                                            atributoNameVisitanteAway[name.text].append(qtde_Fora.text)
                                        else:
                                            atributoNameCasaAway[name.text].append(qtde_Fora.text)
                                            atributoNameVisitanteAway[name.text].append(qtde_Casa.text)
                                except:
                                    if timeDaCasa.lower() == timeAway.lower():
                                        atributoNameCasaAway[name.text]=[qtde_Casa.text]
                                        atributoNameVisitanteAway[name.text]=[qtde_Fora.text]    
                                    else:
                                        atributoNameCasaAway[name.text]=[qtde_Fora.text]
                                        atributoNameVisitanteAway[name.text]=[qtde_Casa.text]     

            dictInformacoesAway = {'timeCasa':{'itens':atributoNameCasaAway},'timeVisitante':{'itens':atributoNameVisitanteAway}}
        except:
            continue


    return dictInformacoesAway

def getTimePrincipal(dados):
    for a in dados.findAll('div', attrs={'class':'card__body card__body--indented'}):
        timeCasa= a.find('span', attrs={'class':'team__name'})
        break

    return timeCasa.text

def getGolsCasaFora(dados):
    golsEmCasa = 0
    golsFora = 0
    casaFora = 'indefinido'

    for x in dados.findAll('tbody'):
        for y in x.findAll('tr'):
            try:
                ehGolEmCasa = y.find('td', attrs={'class':'player home'})
                VariavelLocal = ehGolEmCasa.find('a', attrs={'href':re.compile(r'/futebol.*')})
                if VariavelLocal is not None:
                    casaFora = 'Casa'
                    subGrupoIncidenteIcon = y.find('td', attrs={'class':'incident-icon'})
                    ehGol = subGrupoIncidenteIcon.find('span', attrs={'class':re.compile(r'^goal')}).get('class')
                    print(str(ehGol[1]))
                    '''for z in range(len(x)):
                        teste = x[z]['span']
                        if teste is not None:
                            golsEmCasa = 5'''
            except:
                casaFora = 'fora'
            #teste = y.td.span['sprite-icons goal']
            #teste = ''
                
    '''              try:
                    if y['href']:
                        casaFora = 'Casa'
                except:
                    casaFora = 'Casa'

        for z in dados.findAll('td', attrs={'class':'incident-icon'}):
            try:
                if z.find('span', attrs={'class':re.compile(r'^goal')}):
                    if casaFora == 'Casa':
                        golsEmCasa = golsEmCasa + 1
                    else:
                        golsFora = golsFora + 1
            except:
                continue

        try: 
            if golsEmCasa > 0:
                qtdeGolsEmCasa.append(golsEmCasa) 
        except:''

        try: 
            if golsFora > 0:
                qtdeGolsFora.append(golsFora)
        except: '''
     

def getGolsTime(dados):
    ''
