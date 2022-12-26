from getMatches import getMatch
from getStatsConfrontos import getStatsPartida
from PopularRecord import popularDadosRecordAway
from PopularRecord import popularDadosRecordHome



LinksFake= ['/futebol/europa/liga-europa/sevilla-west-ham/', '/futebol/europa/liga-europa/west-ham-sevilla/']
timeCasa = 'west ham'
clube = timeCasa

dadosConfrontos = getMatch(timeCasa)


links = dadosConfrontos['Links']

dadosDaPartida = getStatsPartida(LinksFake,timeCasa)

records = popularDadosRecordHome(dadosDaPartida,dadosConfrontos,clube,'Casa')





print(str(records))


