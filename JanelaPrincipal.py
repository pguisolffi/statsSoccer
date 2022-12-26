import tkinter as tk
from tkinter import Button, Frame, Label, PhotoImage, StringVar, ttk
from tkinter import messagebox
from tracemalloc import start
from PIL import Image, ImageTk
from PopularRecord import popularDadosRecordAway, popularDadosRecordHome
from getMatches import getMatch
from getStatsConfrontos import getStatsPartidaAway, getStatsPartidaHome


def CriarComboboxParaSelecionarOsTimes(janela):
    lista_Times_Disponivel = ['west ham','manchester city']

    textoCasa = Label(janela, text="Time da Casa")
    textoCasa.place(x=200,y=20)
    #textoCasa.pack()

    timeCasaSelecionado = tk.StringVar()
    combobox_timesDisponiveis = ttk.Combobox(janela, textvariable=timeCasaSelecionado)

    combobox_timesDisponiveis['values'] = lista_Times_Disponivel
    combobox_timesDisponiveis.place(x= 200, y= 40)
    #combobox_timesDisponiveis.pack()
    combobox_timesDisponiveis.current()

    textoVizitante = Label(janela, text="Time Visitante")
    textoVizitante.place(x= 200, y= 70)

    timeVisitanteSelecionado = tk.StringVar()
    combobox_timesDisponiveis = ttk.Combobox(janela, textvariable=timeVisitanteSelecionado)

    combobox_timesDisponiveis['values'] = lista_Times_Disponivel
    combobox_timesDisponiveis.place(x= 200, y= 90)
    combobox_timesDisponiveis.current()

def CriarBotaoAnalisar(janela):
    img = Image.open("C:/Projetos/PY - AnaliseSports/images/btn_play.png")
    img = img.resize((150, 150), Image.ANTIALIAS)
    btnPlayImg = ImageTk.PhotoImage(img)

    botao = Button(janela, command=acaoAnalisar, borderwidth=0,width=120,height=50)
    botao.config(image=btnPlayImg)
    botao.img=btnPlayImg
    botao.place(x= 205, y= 150)

def acaoAnalisar():

    #BARRA DE PROGRESSO E TEXTO INFORMATIVO
    varTextoProgresso = StringVar()
    labelProgresso = Label(janela,textvariable=varTextoProgresso,font=('Arial', 11, 'bold','italic'))
    varTextoProgresso.set('Analisando os dados do time da casa....')
    labelProgresso.place(x=400,y=950)
    barraProgresso = IniciarProgressBar()
    
    #INFORMAÇÕES BUSCADAS DO COMBOBOX
    #LinksFake= ['/futebol/europa/liga-europa/sevilla-west-ham/', '/futebol/europa/liga-europa/west-ham-sevilla/']
    #LinksFakeVisitante= ['/futebol/europa/liga-europa/sevilla-west-ham/', '/futebol/europa/liga-europa/lyon-west-ham/']
    timeCasa = 'Arsenal'
    timeVisitante = 'West ham'

    #ANALISAR O TIME DA CASA
    dadosConfrontosHome = getMatch(timeCasa)
    linksHome = dadosConfrontosHome['Links']
    dadosDaPartidaHome = getStatsPartidaHome(linksHome,timeCasa,barraProgresso)
    recordsHome = popularDadosRecordHome(dadosDaPartidaHome,dadosConfrontosHome,timeCasa)
    popularEstatisticasHome(recordsHome)

    #ANALISAR O TIME VISITANTE
    dadosConfrontosHome.clear()
    #dadosDaPartidaHome.clear()
    #recordsHome.clear()
    varTextoProgresso.set('Iniciando análise do time Visitante....')
    dadosConfrontosAway = getMatch(timeVisitante)
    linksVisitante = dadosConfrontosAway['Links']
    dadosDaPartidaAway = getStatsPartidaAway(linksVisitante,timeVisitante,barraProgresso)
    recordsAway = popularDadosRecordAway(dadosDaPartidaAway,dadosConfrontosAway,timeVisitante)
    popularEstatisticasAway(recordsAway,barraProgresso,varTextoProgresso)

def CriarFrameEstatisticas(janela):
    frame_Home = Frame(janela,bg = "royalblue",bd=10,width=600,height=820, cursor = "target",highlightthickness=2,highlightbackground="black").place(x=600,y=20)
    frame_away = Frame(janela,bg = "orangered",bd=10,width=600,height=820, cursor = "target",highlightthickness=2,highlightbackground="black").place(x=1230,y=20)
    Frame_especiais = Frame(janela,bg = "black",bd=10,width=550,height=595, cursor = "target",highlightthickness=2,highlightbackground="black").place(x=25,y=245)
    return frame_Home,frame_away,Frame_especiais

def CriarLabelEstatisticas(janela):
    #ESTATÍSTICAS TIME DA CASA
    tituloTimeHome = Label(janela,textvariable=time1,font=('Arial', 20, 'bold'), borderwidth=0,background='royalblue')
    time1.set("TIME DA CASA")
    tituloTimeHome.place(x=650,y=50)

    qtdedeJogos1 = Label(janela,textvariable=qtdejogoAnalise1,font=('helvetica 8 underline', 12, 'bold', 'italic'), borderwidth=0,background='royalblue')
    qtdejogoAnalise1.set("últimos Jogos")
    qtdedeJogos1.place(x=650,y=85)

    vitorias1 = Label(janela,textvariable=vitoria1,font=('calibri', 13), borderwidth=0,background='royalblue')
    vitoria1.set("Vitórias \t\t\t\t\t 0 \t0,00%")
    vitorias1.place(x=620,y=150)

    derrotas1 = Label(janela,textvariable=derrota1,font=('calibri', 13), borderwidth=0,background='royalblue')
    derrota1.set("Derrotas\t\t\t\t\t 0\t0,00%")
    derrotas1.place(x=620,y=175)

    empates1 = Label(janela,textvariable=empate1,font=('calibri', 13), borderwidth=0,background='royalblue')
    empate1.set("Empates\t\t\t\t\t 0\t0,00%")
    empates1.place(x=620,y=200)

    mediaGolsFeitos1 = Label(janela,textvariable=medGolsMarcados1,font=('calibri', 13), borderwidth=0,background='royalblue')
    medGolsMarcados1.set("Média de gols marcados\t\t\t 0")
    mediaGolsFeitos1.place(x=620,y=255)

    JogosSemfazer1 = Label(janela,textvariable=JogosSemMarcar1,font=('calibri', 13), borderwidth=0,background='royalblue')
    JogosSemMarcar1.set("Jogos sem marcar gols\t\t\t 0\t0,00%")
    JogosSemfazer1.place(x=620,y=280)

    mediaGolsSofridos1 = Label(janela,textvariable=medGolsSofridos1,font=('calibri', 13), borderwidth=0,background='royalblue')
    medGolsSofridos1.set("Média de gols Sofridos\t\t\t 0")
    mediaGolsSofridos1.place(x=620,y=305)

    JogosSemtomar1 = Label(janela,textvariable=JogosSemSofrer1,font=('calibri', 13), borderwidth=0,background='royalblue')
    JogosSemSofrer1.set("Jogos sem sofrer gols\t\t\t 0\t0,00%")
    JogosSemtomar1.place(x=620,y=330)

    over05Time1 = Label(janela,textvariable=over0_5Time1,font=('calibri', 13), borderwidth=0,background='royalblue')
    over0_5Time1.set("Jogos em que MARCOU 0,5 gols\t\t 0\t0,00%")
    over05Time1.place(x=620,y=385)

    over15Time1 = Label(janela,textvariable=over1_5Time1,font=('calibri', 13), borderwidth=0,background='royalblue')
    over1_5Time1.set("Jogos em que MARCOU 1,5 gols\t\t 0\t0,00%")
    over15Time1.place(x=620,y=410)

    over25Time1 = Label(janela,textvariable=over2_5Time1,font=('calibri', 13), borderwidth=0,background='royalblue')
    over2_5Time1.set("Jogos em que MARCOU 2,5 gols\t\t 0\t0,00%")
    over25Time1.place(x=620,y=435)

    tomou05Time1 = Label(janela,textvariable=tomou0_5Time1,font=('calibri', 13), borderwidth=0,background='royalblue')
    tomou0_5Time1.set("Jogos em que SOFREU 0,5 gols\t\t\t 0\t0,00%")
    tomou05Time1.place(x=620,y=490)

    tomou15Time1 = Label(janela,textvariable=tomou1_5Time1,font=('calibri', 13), borderwidth=0,background='royalblue')
    tomou1_5Time1.set("Jogos em que SOFREU 1,5 gols\t\t\t 0\t0,00%")
    tomou15Time1.place(x=620,y=515)

    tomou25Time1 = Label(janela,textvariable=tomou2_5Time1,font=('calibri', 13), borderwidth=0,background='royalblue')
    tomou2_5Time1.set("Jogos em que SOFREU 0,5 gols\t\t\t 0\t0,00%")
    tomou25Time1.place(x=620,y=540)

    escanteio1 = Label(janela,textvariable=escanteioTime1,font=('calibri', 13), borderwidth=0,background='royalblue')
    escanteioTime1.set("Escanteios (média)\t\t\t\t 0")
    escanteio1.place(x=620,y=595)

    chuteGolTime1 = Label(janela,textvariable=chuteaGolTime1,font=('calibri', 13), borderwidth=0,background='royalblue')
    chuteaGolTime1.set("Chutes a gols (média)\t\t\t 0")
    chuteGolTime1.place(x=620,y=620)

    chutepForaTime1 = Label(janela,textvariable=chuteForaTime1,font=('calibri', 13), borderwidth=0,background='royalblue')
    chuteForaTime1.set("Chutes pra fora (média)\t\t\t 0")
    chutepForaTime1.place(x=620,y=645)

    finalizacoesTime1 = Label(janela,textvariable=finalizacaoTime1,font=('calibri', 13), borderwidth=0,background='royalblue')
    finalizacaoTime1.set("Finalizações (média)\t\t\t\t 0")
    finalizacoesTime1.place(x=620,y=670)

    impedimentosTime1 = Label(janela,textvariable=impedimentoTime1,font=('calibri', 13), borderwidth=0,background='royalblue')
    impedimentoTime1.set("Impedimentos (média)\t\t\t 0")
    impedimentosTime1.place(x=620,y=695)

    laterais1 = Label(janela,textvariable=lateral1,font=('calibri', 13), borderwidth=0,background='royalblue')
    lateral1.set("Laterais (média)\t\t\t\t 0")
    laterais1.place(x=620,y=720)

    tirosdeMeta1 = Label(janela,textvariable=tirodeMeta1,font=('calibri', 13), borderwidth=0,background='royalblue')
    tirodeMeta1.set("Tiros de meta (média)\t\t\t 0")
    tirosdeMeta1.place(x=620,y=745)

    faltas1 = Label(janela,textvariable=falta1,font=('calibri', 13), borderwidth=0,background='royalblue')
    falta1.set("Faltas (média)\t\t\t\t 0")
    faltas1.place(x=620,y=770)

    cartoesAmarelo1 = Label(janela,textvariable=cartaoAmarelo1,font=('calibri', 13), borderwidth=0,background='royalblue')
    cartaoAmarelo1.set("Cartões Amarelos (média)\t\t\t 0")
    cartoesAmarelo1.place(x=620,y=795)


    #ESTATÍSTICAS TIME VISITANTE
    tituloTimeAway = Label(janela,textvariable=time2,font=('Arial', 20, 'bold'), borderwidth=0,background='orangered')
    time2.set("TIME VISITANTE")
    tituloTimeAway.place(x=1275,y=50)

    qtdedeJogos2 = Label(janela,textvariable=qtdeJogoAnalise2,font=('helvetica 8 underline', 12, 'bold', 'italic'), borderwidth=0,background='orangered')
    qtdeJogoAnalise2.set("últimos Jogos")
    qtdedeJogos2.place(x=1280,y=85)

    vitorias2 = Label(janela,textvariable=vitoria2,font=('calibri', 13), borderwidth=0,background='orangered')
    vitoria2.set("Vitórias \t\t\t\t\t 0 \t0,00%")
    vitorias2.place(x=1250,y=150)

    derrotas2 = Label(janela,textvariable=derrota2,font=('calibri', 13), borderwidth=0,background='orangered')
    derrota2.set("Derrotas\t\t\t\t\t 0\t0,00%")
    derrotas2.place(x=1250,y=175)

    empates2 = Label(janela,textvariable=empate2,font=('calibri', 13), borderwidth=0,background='orangered')
    empate2.set("Empates\t\t\t\t\t 0\t0,00%")
    empates2.place(x=1250,y=200)

    mediaGolsFeitos2 = Label(janela,textvariable=medGolsMarcados2,font=('calibri', 13), borderwidth=0,background='orangered')
    medGolsMarcados2.set("Média de gols marcados\t\t\t 0")
    mediaGolsFeitos2.place(x=1250,y=255)

    JogosSemfazer2 = Label(janela,textvariable=JogosSemMarcar2,font=('calibri', 13), borderwidth=0,background='orangered')
    JogosSemMarcar2.set("Jogos sem marcar gols\t\t\t 0\t0,00%")
    JogosSemfazer2.place(x=1250,y=280)

    mediaGolsSofridos2 = Label(janela,textvariable=medGolsSofridos2,font=('calibri', 13), borderwidth=0,background='orangered')
    medGolsSofridos2.set("Média de gols Sofridos\t\t\t 0")
    mediaGolsSofridos2.place(x=1250,y=305)

    JogosSemtomar2 = Label(janela,textvariable=JogosSemSofrer2,font=('calibri', 13), borderwidth=0,background='orangered')
    JogosSemSofrer2.set("Jogos sem sofrer gols\t\t\t 0\t0,00%")
    JogosSemtomar2.place(x=1250,y=330)

    over05Time2 = Label(janela,textvariable=over0_5Time2,font=('calibri', 13), borderwidth=0,background='orangered')
    over0_5Time2.set("Jogos em que MARCOU 0,5 gols\t\t 0\t0,00%")
    over05Time2.place(x=1250,y=385)

    over15Time2 = Label(janela,textvariable=over1_5Time2,font=('calibri', 13), borderwidth=0,background='orangered')
    over1_5Time2.set("Jogos em que MARCOU 1,5 gols\t\t 0\t0,00%")
    over15Time2.place(x=1250,y=410)

    over25Time2 = Label(janela,textvariable=over2_5Time2,font=('calibri', 13), borderwidth=0,background='orangered')
    over2_5Time2.set("Jogos em que MARCOU 2,5 gols\t\t 0\t0,00%")
    over25Time2.place(x=1250,y=435)

    tomou05Time2 = Label(janela,textvariable=tomou0_5Time2,font=('calibri', 13), borderwidth=0,background='orangered')
    tomou0_5Time2.set("Jogos em que SOFREU 0,5 gols\t\t\t 0\t0,00%")
    tomou05Time2.place(x=1250,y=490)

    tomou15Time2 = Label(janela,textvariable=tomou1_5Time2,font=('calibri', 13), borderwidth=0,background='orangered')
    tomou1_5Time2.set("Jogos em que SOFREU 1,5 gols\t\t\t 0\t0,00%")
    tomou15Time2.place(x=1250,y=515)

    tomou25Time2 = Label(janela,textvariable=tomou2_5Time2,font=('calibri', 13), borderwidth=0,background='orangered')
    tomou2_5Time2.set("Jogos em que SOFREU 0,5 gols\t\t\t 0\t0,00%")
    tomou25Time2.place(x=1250,y=540)

    escanteio2 = Label(janela,textvariable=escanteioTime2,font=('calibri', 13), borderwidth=0,background='orangered')
    escanteioTime2.set("Escanteios (média)\t\t\t\t 0")
    escanteio2.place(x=1250,y=595)

    chuteGolTime2 = Label(janela,textvariable=chuteaGolTime2,font=('calibri', 13), borderwidth=0,background='orangered')
    chuteaGolTime2.set("Chutes a gols (média)\t\t\t 0")
    chuteGolTime2.place(x=1250,y=620)

    chutepForaTime2 = Label(janela,textvariable=chuteForaTime2,font=('calibri', 13), borderwidth=0,background='orangered')
    chuteForaTime2.set("Chutes pra fora (média)\t\t\t 0")
    chutepForaTime2.place(x=1250,y=645)

    finalizacoesTime2 = Label(janela,textvariable=finalizacaoTime2,font=('calibri', 13), borderwidth=0,background='orangered')
    finalizacaoTime2.set("Finalizações (média)\t\t\t\t 0")
    finalizacoesTime2.place(x=1250,y=670)

    impedimentosTime2 = Label(janela,textvariable=impedimentoTime2,font=('calibri', 13), borderwidth=0,background='orangered')
    impedimentoTime2.set("Impedimentos (média)\t\t\t 0")
    impedimentosTime2.place(x=1250,y=695)

    laterais2 = Label(janela,textvariable=lateral2,font=('calibri', 13), borderwidth=0,background='orangered')
    lateral2.set("Laterais (média)\t\t\t\t 0")
    laterais2.place(x=1250,y=720)

    tirosdeMeta2 = Label(janela,textvariable=tirodeMeta2,font=('calibri', 13), borderwidth=0,background='orangered')
    tirodeMeta2.set("Tiros de meta (média)\t\t\t 0")
    tirosdeMeta2.place(x=1250,y=745)

    faltas2 = Label(janela,textvariable=falta2,font=('calibri', 13), borderwidth=0,background='orangered')
    falta2.set("Faltas (média)\t\t\t\t 0")
    faltas2.place(x=1250,y=770)

    cartoesAmarelo2 = Label(janela,textvariable=cartaoAmarelo2,font=('calibri', 13), borderwidth=0,background='orangered')
    cartaoAmarelo2.set("Cartões Amarelos (média)\t\t\t 0")
    cartoesAmarelo2.place(x=1250,y=795)

    #OPORTUNIDADES
    tituloEspeciais = Label(janela,textvariable=Oportunidade,font=('Arial', 20, 'bold'), borderwidth=0,background='black',foreground='gold')
    Oportunidade.set("Oportunidades Identificadas")
    tituloEspeciais.place(x=100,y=265)

def IniciarProgressBar():
    pb = ttk.Progressbar(janela,orient='horizontal',mode='determinate',length=1000)
    pb.place(x=400,y=900)
    pb['value'] = 1
    pb.update()
 
    return pb

def CalcularPercentual(jogos,iten):
    calculo = (iten / jogos)*100
    percent = f"{calculo:.2f}%"
    return percent

def popularEstatisticasHome(recodHome):
    time1.set(recodHome.time.upper())
    qtdejogoAnalise1.set(f"últimos {recodHome.qtdeJogos} Jogos")
    percentualVitoria = CalcularPercentual(recodHome.qtdeJogos,recodHome.Vitórias)
    vitoria1.set(f"Vitórias \t\t\t\t\t {recodHome.Vitórias} \t{percentualVitoria}")
    percentualDerrota = CalcularPercentual(recodHome.qtdeJogos,recodHome.Derrotas)
    derrota1.set(f"Derrotas\t\t\t\t\t {recodHome.Derrotas}\t{percentualDerrota}")
    percentualEmpate = CalcularPercentual(recodHome.qtdeJogos,recodHome.Empates)
    empate1.set(f"Empates\t\t\t\t\t {recodHome.Empates}\t{percentualEmpate}")
    medGolsMarcados1.set(f"Média de gols marcados\t\t\t {recodHome.MediaGolsMarcados}")
    medGolsSofridos1.set(f"Média de gols Sofridos\t\t\t {recodHome.MediaGolsSofridos}")
    percentualSemMarcar = CalcularPercentual(recodHome.qtdeJogos,recodHome.JogosSemMarcar)
    JogosSemMarcar1.set(f"Jogos sem marcar gols\t\t\t {recodHome.JogosSemMarcar}\t{percentualSemMarcar}")
    percentualSemSofrer = CalcularPercentual(recodHome.qtdeJogos,recodHome.JogosSemSofrer)
    JogosSemSofrer1.set(f"Jogos sem sofrer gols\t\t\t {recodHome.JogosSemSofrer}\t{percentualSemSofrer}")
    percentualOver05 = CalcularPercentual(recodHome.qtdeJogos,recodHome.MarcouOver0_5)
    over0_5Time1.set(f"Jogos em que MARCOU 0,5 gols\t\t {recodHome.MarcouOver0_5}\t{percentualOver05}")
    percentualOver15 = CalcularPercentual(recodHome.qtdeJogos,recodHome.MarcouOver1_5)   
    over1_5Time1.set(f"Jogos em que MARCOU 1,5 gols\t\t {recodHome.MarcouOver1_5}\t{percentualOver15}")
    percentualOver25 = CalcularPercentual(recodHome.qtdeJogos,recodHome.MarcouOver2_5) 
    over2_5Time1.set(f"Jogos em que MARCOU 2,5 gols\t\t {recodHome.MarcouOver2_5}\t{percentualOver25}")
    percentualTomou05 = CalcularPercentual(recodHome.qtdeJogos,recodHome.Sofreu0_5)  
    tomou0_5Time1.set(f"Jogos em que SOFREU 0,5 gols\t\t\t {recodHome.Sofreu0_5}\t{percentualTomou05}")
    percentualTomou15 = CalcularPercentual(recodHome.qtdeJogos,recodHome.Sofreu1_5)      
    tomou1_5Time1.set(f"Jogos em que SOFREU 1,5 gols\t\t\t {recodHome.Sofreu1_5}\t{percentualTomou15}")
    percentualTomou25 = CalcularPercentual(recodHome.qtdeJogos,recodHome.Sofreu2_5)
    tomou2_5Time1.set(f"Jogos em que SOFREU 2,5 gols\t\t\t {recodHome.Sofreu2_5}\t{percentualTomou25}")
    escanteioTime1.set(f"Escanteios (média)\t\t\t\t {recodHome.Escanteios}")
    chuteaGolTime1.set(f"Chutes a gols (média)\t\t\t {recodHome.ChutesNoGol}")
    chuteForaTime1.set(f"Chutes pra fora (média)\t\t\t {recodHome.ChutesPraFora}")
    finalizacaoTime1.set(f"Finalizações (média)\t\t\t\t {recodHome.Finalizacoes}")
    impedimentoTime1.set(f"Impedimentos (média)\t\t\t {recodHome.Impedimentos}")
    lateral1.set(f"Laterais (média)\t\t\t\t {recodHome.Laterais}")
    tirodeMeta1.set(f"Tiros de meta (média)\t\t\t {recodHome.TiroDeMeta}")
    falta1.set(f"Faltas (média)\t\t\t\t {recodHome.Faltas}")
    cartaoAmarelo1.set(f"Cartões Amarelos (média)\t\t\t {recodHome.CartoesAmarelos}")
    
def popularEstatisticasAway(recodAway,barraProgresso,varTextoProgresso):
    time2.set(recodAway.time.upper())
    qtdeJogoAnalise2.set(f"últimos {recodAway.qtdeJogos} Jogos")
    percentualVitoria = CalcularPercentual(recodAway.qtdeJogos,recodAway.Vitórias)
    vitoria2.set(f"Vitórias \t\t\t\t\t {recodAway.Vitórias} \t{percentualVitoria}")
    percentualDerrota = CalcularPercentual(recodAway.qtdeJogos,recodAway.Derrotas)
    derrota2.set(f"Derrotas\t\t\t\t\t {recodAway.Derrotas}\t{percentualDerrota}")
    percentualEmpate = CalcularPercentual(recodAway.qtdeJogos,recodAway.Empates)
    empate2.set(f"Empates\t\t\t\t\t {recodAway.Empates}\t{percentualEmpate}")
    medGolsMarcados2.set(f"Média de gols marcados\t\t\t {recodAway.MediaGolsMarcados}")
    medGolsSofridos2.set(f"Média de gols Sofridos\t\t\t {recodAway.MediaGolsSofridos}")
    percentualSemMarcar = CalcularPercentual(recodAway.qtdeJogos,recodAway.JogosSemMarcar)
    JogosSemMarcar2.set(f"Jogos sem marcar gols\t\t\t {recodAway.JogosSemMarcar}\t{percentualSemMarcar}")
    percentualSemSofrer = CalcularPercentual(recodAway.qtdeJogos,recodAway.JogosSemSofrer)
    JogosSemSofrer2.set(f"Jogos sem sofrer gols\t\t\t {recodAway.JogosSemSofrer}\t{percentualSemSofrer}")
    percentualOver05 = CalcularPercentual(recodAway.qtdeJogos,recodAway.MarcouOver0_5)
    over0_5Time2.set(f"Jogos em que MARCOU 0,5 gols\t\t {recodAway.MarcouOver0_5}\t{percentualOver05}")
    percentualOver15 = CalcularPercentual(recodAway.qtdeJogos,recodAway.MarcouOver1_5)   
    over1_5Time2.set(f"Jogos em que MARCOU 1,5 gols\t\t {recodAway.MarcouOver1_5}\t{percentualOver15}")
    percentualOver25 = CalcularPercentual(recodAway.qtdeJogos,recodAway.MarcouOver2_5) 
    over2_5Time2.set(f"Jogos em que MARCOU 2,5 gols\t\t {recodAway.MarcouOver2_5}\t{percentualOver25}")
    percentualTomou05 = CalcularPercentual(recodAway.qtdeJogos,recodAway.Sofreu0_5)  
    tomou0_5Time2.set(f"Jogos em que SOFREU 0,5 gols\t\t\t {recodAway.Sofreu0_5}\t{percentualTomou05}")
    percentualTomou15 = CalcularPercentual(recodAway.qtdeJogos,recodAway.Sofreu1_5)      
    tomou1_5Time2.set(f"Jogos em que SOFREU 1,5 gols\t\t\t {recodAway.Sofreu1_5}\t{percentualTomou15}")
    percentualTomou25 = CalcularPercentual(recodAway.qtdeJogos,recodAway.Sofreu2_5)
    tomou2_5Time2.set(f"Jogos em que SOFREU 2,5 gols\t\t\t {recodAway.Sofreu2_5}\t{percentualTomou25}")
    escanteioTime2.set(f"Escanteios (média)\t\t\t\t {recodAway.Escanteios}")
    chuteaGolTime2.set(f"Chutes a gols (média)\t\t\t {recodAway.ChutesNoGol}")
    chuteForaTime2.set(f"Chutes pra fora (média)\t\t\t {recodAway.ChutesPraFora}")
    finalizacaoTime2.set(f"Finalizações (média)\t\t\t\t {recodAway.Finalizacoes}")
    impedimentoTime2.set(f"Impedimentos (média)\t\t\t {recodAway.Impedimentos}")
    lateral2.set(f"Laterais (média)\t\t\t\t {recodAway.Laterais}")
    tirodeMeta2.set(f"Tiros de meta (média)\t\t\t {recodAway.TiroDeMeta}")
    falta2.set(f"Faltas (média)\t\t\t\t {recodAway.Faltas}")
    cartaoAmarelo2.set(f"Cartões Amarelos (média)\t\t\t {recodAway.CartoesAmarelos}")
    barraProgresso.destroy()
    varTextoProgresso.set('')


janela = tk.Tk()
janela.state("zoomed")
janela.title("Estatísticas e analises de confronto")

#stringVars
#time1, time2, qtdejogoAnalise1,qtdeJogoAnalise2,vitoria1,derrota1,empate1,medGolsMarcados1,medGolsSofridos1,JogosSemMarcar1,over0_5Time1,over1_5Time1,over2_5Time1,tomou0_5Time1,tomou1_5Time1,tomou2_5Time1,escanteioTime1,chuteaGolTime1,chuteForaTime1,finalizacaoTime1,impedimentoTime1,lateral1,tirodeMeta1,falta1,cartaoAmarelo1,cartaoVermelho1,vitoria2,derrota2,empate2,medGolsMarcados2,medGolsSofridos2,JogosSemMarcar2,over0_5Time2,over1_5Time2,over2_5Time2,tomou0_5Time2,tomou1_5Time2,tomou2_5Time2,escanteioTime2,chuteaGolTime2,chuteForaTime2,finalizacaoTime2,impedimentoTime2,lateral2,tirodeMeta2,falta2,cartaoAmarelo2,cartaoVermelho2 = StringVar()
time1 = StringVar()
time2 = StringVar()
Oportunidade = StringVar()
qtdejogoAnalise1 = StringVar()
qtdeJogoAnalise2 = StringVar()
vitoria1 = StringVar()
derrota1 = StringVar()
empate1 = StringVar()
medGolsMarcados1 = StringVar()
medGolsSofridos1 = StringVar()
JogosSemMarcar1 = StringVar()
JogosSemSofrer1 = StringVar()
over0_5Time1 = StringVar()
over1_5Time1 = StringVar()
over2_5Time1 = StringVar()
tomou0_5Time1 = StringVar()
tomou1_5Time1 = StringVar()
tomou2_5Time1 = StringVar()
escanteioTime1 = StringVar()
chuteaGolTime1 = StringVar()
chuteForaTime1 = StringVar()
finalizacaoTime1 = StringVar()
impedimentoTime1 = StringVar()
lateral1 = StringVar()
tirodeMeta1 = StringVar()
falta1 = StringVar()
cartaoAmarelo1 = StringVar()
vitoria2 = StringVar()
derrota2 = StringVar()
empate2 = StringVar()
medGolsMarcados2 = StringVar()
medGolsSofridos2 = StringVar()
JogosSemMarcar2 = StringVar()
JogosSemSofrer2 = StringVar()
over0_5Time2 = StringVar()
over1_5Time2 = StringVar()
over2_5Time2 = StringVar()
tomou0_5Time2 = StringVar()
tomou1_5Time2 = StringVar()
tomou2_5Time2 = StringVar()
escanteioTime2 = StringVar()
chuteaGolTime2 = StringVar()
chuteForaTime2 = StringVar()
finalizacaoTime2 = StringVar()
impedimentoTime2 = StringVar()
lateral2 = StringVar()
tirodeMeta2 = StringVar()
falta2 = StringVar()
cartaoAmarelo2 = StringVar()

pb = StringVar()

CriarComboboxParaSelecionarOsTimes(janela)
CriarBotaoAnalisar(janela)
CriarFrameEstatisticas(janela)
CriarLabelEstatisticas(janela)

janela.mainloop()



