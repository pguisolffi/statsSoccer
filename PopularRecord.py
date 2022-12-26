import Records_dados  

def popularDadosRecordHome(dadosDaPartida,dadosDosConfrontosHome,clube):

    Records_dados.dadosHome.time = clube
    Records_dados.dadosHome.qtdeJogos = len(dadosDosConfrontosHome[clube]['Gols Marcados'])
    Records_dados.dadosHome.Vitórias = getNumberVitorias(dadosDosConfrontosHome[clube])
    Records_dados.dadosHome.Derrotas = getNumberDerrotas(dadosDosConfrontosHome[clube])
    Records_dados.dadosHome.Empates = getNumberEmpates(dadosDosConfrontosHome[clube])
    Records_dados.dadosHome.MediaGolsMarcados = getMedia(dadosDosConfrontosHome[clube]['Gols Marcados'])
    Records_dados.dadosHome.JogosSemMarcar = jogosSemSofreOuMarcar(dadosDosConfrontosHome[clube]['Gols Marcados'])
    Records_dados.dadosHome.MediaGolsSofridos = getMedia(dadosDosConfrontosHome[clube]['Gols Sofridos'])
    Records_dados.dadosHome.JogosSemSofrer = jogosSemSofreOuMarcar(dadosDosConfrontosHome[clube]['Gols Sofridos'])
    Records_dados.dadosHome.MarcouOver0_5 = getQtdesMaiores(dadosDosConfrontosHome[clube]['Gols Marcados'], 0.5)
    Records_dados.dadosHome.MarcouOver1_5 = getQtdesMaiores(dadosDosConfrontosHome[clube]['Gols Marcados'], 1.5)
    Records_dados.dadosHome.MarcouOver2_5 = getQtdesMaiores(dadosDosConfrontosHome[clube]['Gols Marcados'], 2.5)
    Records_dados.dadosHome.Sofreu0_5 = getQtdesMaiores(dadosDosConfrontosHome[clube]['Gols Sofridos'], 0.5)
    Records_dados.dadosHome.Sofreu1_5 = getQtdesMaiores(dadosDosConfrontosHome[clube]['Gols Sofridos'], 1.5)
    Records_dados.dadosHome.Sofreu2_5 = getQtdesMaiores(dadosDosConfrontosHome[clube]['Gols Sofridos'], 2.5) 

    try:     
        Records_dados.dadosHome.ChutesNoGol = getMedia(dadosDaPartida['timeCasa']['itens']['Chutes a gol'])
        Records_dados.dadosHome.Escanteios = getMedia(dadosDaPartida['timeCasa']['itens']['Escanteio'])
        Records_dados.dadosHome.ChutesPraFora = getMedia(dadosDaPartida['timeCasa']['itens']['Chutes fora'])
        Records_dados.dadosHome.Finalizacoes = getFinalizacoes(dadosDaPartida['timeCasa']['itens']['Chutes a gol'],dadosDaPartida['timeCasa']['itens']['Chutes fora'])
        Records_dados.dadosHome.Impedimentos = getMedia(dadosDaPartida['timeCasa']['itens']['Impedimentos'])
        Records_dados.dadosHome.Laterais = getMedia(dadosDaPartida['timeCasa']['itens']['Laterais'])
        Records_dados.dadosHome.TiroDeMeta = getMedia(dadosDaPartida['timeCasa']['itens']['Tiro de meta'])
        Records_dados.dadosHome.Faltas = getMedia(dadosDaPartida['timeCasa']['itens']['Faltas'])
        Records_dados.dadosHome.CartoesAmarelos = getMedia(dadosDaPartida['timeCasa']['itens']['Catões amarelos'])
        Records_dados.dadosHome.CartoesVermelhos = getMedia(dadosDaPartida['timeCasa']['itens']['Catões vermelhos'])
    except:
        Records_dados.dadosHome.ChutesNoGol = 'indisp.'
        Records_dados.dadosHome.Escanteios = 'indisp.'
        Records_dados.dadosHome.ChutesPraFora = 'indisp.'
        Records_dados.dadosHome.Finalizacoes = 'indisp.'
        Records_dados.dadosHome.Impedimentos = 'indisp.'
        Records_dados.dadosHome.Laterais = 'indisp.'
        Records_dados.dadosHome.TiroDeMeta = 'indisp.'
        Records_dados.dadosHome.Faltas = 'indisp.'
        Records_dados.dadosHome.CartoesAmarelos = 'indisp.'
        Records_dados.dadosHome.CartoesVermelhos = 'indisp.'

    return Records_dados.dadosHome
    
def popularDadosRecordAway(dadosDaPartida,dadosDosConfrontos,clube):
    Records_dados.dadosVisitante.time = clube
    Records_dados.dadosVisitante.qtdeJogos = len(dadosDosConfrontos[clube]['Gols Marcados'])
    Records_dados.dadosVisitante.Vitórias = getNumberVitorias(dadosDosConfrontos[clube])
    Records_dados.dadosVisitante.Derrotas = getNumberDerrotas(dadosDosConfrontos[clube])
    Records_dados.dadosVisitante.Empates = getNumberEmpates(dadosDosConfrontos[clube])
    Records_dados.dadosVisitante.MediaGolsMarcados = getMedia(dadosDosConfrontos[clube]['Gols Marcados'])
    Records_dados.dadosVisitante.JogosSemMarcar = jogosSemSofreOuMarcar(dadosDosConfrontos[clube]['Gols Marcados'])
    Records_dados.dadosVisitante.MediaGolsSofridos = getMedia(dadosDosConfrontos[clube]['Gols Sofridos'])
    Records_dados.dadosVisitante.JogosSemSofrer = jogosSemSofreOuMarcar(dadosDosConfrontos[clube]['Gols Sofridos'])
    Records_dados.dadosVisitante.MarcouOver0_5 = getQtdesMaiores(dadosDosConfrontos[clube]['Gols Marcados'], 0.5)
    Records_dados.dadosVisitante.MarcouOver1_5 = getQtdesMaiores(dadosDosConfrontos[clube]['Gols Marcados'], 1.5)
    Records_dados.dadosVisitante.MarcouOver2_5 = getQtdesMaiores(dadosDosConfrontos[clube]['Gols Marcados'], 2.5)
    Records_dados.dadosVisitante.Sofreu0_5 = getQtdesMaiores(dadosDosConfrontos[clube]['Gols Sofridos'], 0.5)
    Records_dados.dadosVisitante.Sofreu1_5 = getQtdesMaiores(dadosDosConfrontos[clube]['Gols Sofridos'], 1.5)
    Records_dados.dadosVisitante.Sofreu2_5 = getQtdesMaiores(dadosDosConfrontos[clube]['Gols Sofridos'], 2.5)
    
    try:
        Records_dados.dadosVisitante.ChutesNoGol = getMedia(dadosDaPartida['timeVisitante']['itens']['Chutes a gol'])
        Records_dados.dadosVisitante.Escanteios = getMedia(dadosDaPartida['timeVisitante']['itens']['Escanteio'])
        Records_dados.dadosVisitante.ChutesPraFora = getMedia(dadosDaPartida['timeVisitante']['itens']['Chutes fora'])
        Records_dados.dadosVisitante.Finalizacoes = getFinalizacoes(dadosDaPartida['timeVisitante']['itens']['Chutes a gol'],dadosDaPartida['timeVisitante']['itens']['Chutes fora'])
        Records_dados.dadosVisitante.Impedimentos = getMedia(dadosDaPartida['timeVisitante']['itens']['Impedimentos'])
        Records_dados.dadosVisitante.Laterais = getMedia(dadosDaPartida['timeVisitante']['itens']['Laterais'])
        Records_dados.dadosVisitante.TiroDeMeta = getMedia(dadosDaPartida['timeVisitante']['itens']['Tiro de meta'])
        Records_dados.dadosVisitante.Faltas = getMedia(dadosDaPartida['timeVisitante']['itens']['Faltas'])
        Records_dados.dadosVisitante.CartoesAmarelos = getMedia(dadosDaPartida['timeVisitante']['itens']['Catões amarelos'])
        Records_dados.dadosVisitante.CartoesVermelhos = getMedia(dadosDaPartida['timeVisitante']['itens']['Catões vermelhos'])
    except:
        Records_dados.dadosVisitante.ChutesNoGol = 'indisp.'
        Records_dados.dadosVisitante.Escanteios = 'indisp.'
        Records_dados.dadosVisitante.ChutesPraFora = 'indisp.'
        Records_dados.dadosVisitante.Finalizacoes = 'indisp.'
        Records_dados.dadosVisitante.Impedimentos = 'indisp.'
        Records_dados.dadosVisitante.Laterais = 'indisp.'
        Records_dados.dadosVisitante.TiroDeMeta = 'indisp.'
        Records_dados.dadosVisitante.Faltas = 'indisp.'
        Records_dados.dadosVisitante.CartoesAmarelos = 'indisp.'
        Records_dados.dadosVisitante.CartoesVermelhos = 'indisp.'
    
    return Records_dados.dadosVisitante

def getMedia(lista):
    media = sum(map(int,lista)) / len(lista)
    mediaFormatada = f"{media:.2f}"
    return mediaFormatada
    
def getFinalizacoes(listaChutesGol,listaChutesFora):
    Mediafinalizacao = (sum(map(int,listaChutesGol)) + sum(map(int,listaChutesFora))) / (len(listaChutesFora))
    mediaFinalizacaoFormatada = f"{Mediafinalizacao:.2f}"
    return mediaFinalizacaoFormatada

def getNumberVitorias(lista):
    x = 0
    qtdeVitorias = 0
    for x in range(len(lista['Gols Marcados'])):
            if lista['Gols Marcados'][x] > lista['Gols Sofridos'][x]:
                qtdeVitorias = qtdeVitorias + 1
    return qtdeVitorias

def getNumberDerrotas(lista):
    x = 0
    qtdeDerrotas = 0
    for x in range(len(lista['Gols Marcados'])):
            if lista['Gols Marcados'][x] < lista['Gols Sofridos'][x]:
                qtdeDerrotas = qtdeDerrotas + 1
    return qtdeDerrotas

def getNumberEmpates(lista):
    x = 0
    qtdeEmpates = 0
    for x in range(len(lista['Gols Marcados'])):
        if lista['Gols Marcados'][x] == lista['Gols Sofridos'][x]:
            qtdeEmpates = qtdeEmpates + 1
    return qtdeEmpates

def getQtdesMaiores(lista,numeroComparativo):
    qtdeMaior = sum(i>numeroComparativo for i in map(int,lista))
    return qtdeMaior

def jogosSemSofreOuMarcar(lista):
    qtde = sum(i==0 for i in map(int,lista))
    return qtde