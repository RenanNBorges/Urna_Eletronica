import objetos
from graphics import *
import os
caminho = os.getcwd()
pathCargoFile = [caminho + '/data/candidatos/senador.csv',caminho + '/data/candidatos/presidente.csv',]
cargoVtos = [caminho + '/data/candidatos/votos/voto_senador.csv',caminho + '/data/candidatos/votos/voto_presidente.csv']
n_eleitoral_list = []
n_eleitoral = [0]
nome_list = []
vice_list = []
partido_list = []
foto_list = []
fotovice_list = []

def cargoFile(cargo):
    return pathCargoFile[cargo-1]
def reset_listas():
    del n_eleitoral_list[:]
    del n_eleitoral[:]
    del nome_list[:]
    del partido_list[:]
    del vice_list[:]
    del foto_list[:]
    del fotovice_list[:]

def lista_candidatos(telaAtual):
        arquivo = open(cargoFile(telaAtual),'r',encoding='utf-8')
        listaCandidatos = arquivo.read()

        listaCandidatos = listaCandidatos.split("\n")
        arquivo.close()
        
        for candidatos in listaCandidatos[1:]:
            candidato = candidatos.split(";")
            n_eleitoral_list.append(candidato[0])
            nome_list.append(candidato[1])
            partido_list.append(candidato[2])
            vice_list.append(candidato[3])
            foto_list.append(caminho + candidato[4])
            fotovice_list.append(caminho + candidato[5])

        
        return n_eleitoral_list

def valido(VOTO,telaAtual):
    
    if telaAtual != 3:
        n_eleitoral = lista_candidatos(telaAtual)
        for i in range(len(n_eleitoral)):
            print(n_eleitoral,VOTO)
            if VOTO == n_eleitoral[i]:
                return "valido"
            
        reset_listas()
        return "nulo"
    else:
        return 0
    
def infos(VOTO,CARGO):
    n_eleitoral = [0]
    del n_eleitoral[:]
    n_eleitoral = lista_candidatos(CARGO)

    for i in range(len(n_eleitoral)):

        if VOTO == n_eleitoral[i]:
            
            nome_candidato = nome_list[i] 
            partido_candidato = partido_list[i] 
            vice_candidato = vice_list[i]
            foto_candidato = foto_list[i] 
            fotovice_candidato = fotovice_list[i]
            return nome_candidato, partido_candidato,vice_candidato,foto_candidato,fotovice_candidato

def display(voto,telaAtual):
    reset_listas()
    nome, partido,vice,foto,fotovice = infos(voto,telaAtual)

    cargo = {1:"Senador",2:"Presidente"}
    cargoVice = {1:"Suplente",2:"Vice-Presidente"}
    foto_obj = Image(Point(555-44.5,213+62),foto)
    fotovice_obj = Image(Point(555-37,450),fotovice)
    cargo_txt = Text(Point(555-44.5,213+140),cargo[telaAtual])
    cargo_txt.setSize(11)
    cargo_vice_txt = Text(Point(555-35,213+290),cargoVice[telaAtual])
    cargo_vice_txt.setSize(6)
    nome_obj = Text(Point(135,213+135),nome)
    partido_obj = Text(Point(135,213+165),partido)
    vice_obj = Text(Point(135,213+205),vice)
    candidato_display = [foto_obj,fotovice_obj,cargo_txt,cargo_vice_txt,nome_obj,partido_obj,vice_obj]
    reset_listas()
    return candidato_display


def initVotos():
    for i in range(len(cargoVtos)):
        n_eleitoral = lista_candidatos(i+1)
        votos_arquivo = open(cargoVtos[i],'w+',encoding='utf-8')
        for i in n_eleitoral:
            candidato = i + ';'
            votos_arquivo.write(candidato)
        votos_arquivo.write("\n")
        for i in range(len(n_eleitoral)):
            if i == len(n_eleitoral)-1:
                num = "0"
            else:
                num = "0" + ';'
            votos_arquivo.write(num)
        votos_arquivo.close()
        del n_eleitoral[:]


def votos(VOTO,CARGO):
    n_eleitoral = lista_candidatos(CARGO)
    votos_arquivo = open(cargoVtos[CARGO-1],'r+',encoding='utf-8')
    qtd_votos = votos_arquivo.readlines()
    texto = len(qtd_votos[0]) + 1
    qtd_votos = qtd_votos[1].split(';')

    for i in range(len(n_eleitoral)):
        if VOTO == n_eleitoral[i]:
            qtd_votos[i] = int(qtd_votos[i]) + 1
            break
        else:
            continue
    votos_arquivo.seek(texto) 
    for i in range(len(qtd_votos)):
        if i == len(qtd_votos)-1:
            a =  str(qtd_votos[i])
        else:
            a =  str(qtd_votos[i]) + ';'
        votos_arquivo.write(a)

    votos_arquivo.close()
    del n_eleitoral[:]

def resultado_votacao():
    candidatos_legiveis = {"12":"CIRO GOMES","13":"LULA","14":"PADRE KELMON","15":"SIMONE TEBET","16":"VERA","21":"SOFIA MANZANO","22":"JAIR BOLSONARO","27":"CONSTITUINTE EYMAEL","30":"FELIPE D'AVILA","44":"SORAYA THRONICKE","80":"LÉO PÉRICLES","555":"ANA AMÉLIA LEMOS","160":"FABIANA SANGUINÉ","100":"HAMILTON MOURÃO","200":"MARISTELA ZANOTTO","131":"OLÍVIO DUTRA","270":"PAULO ROSA","700":"PROFESSOR NADO","400":"SANNY FIGUEIREDO","Branco":"Branco","Nulo":"Nulo"}
    for CARGO in range(len(pathCargoFile)):
        with open(cargoVtos[CARGO],"r",encoding="utf8") as cargoFile:
            lista = cargoFile.readlines()
            totalDeVotos_list = lista[1].split(";")
            totalDeVotos = int(totalDeVotos_list[0])
            for voto in totalDeVotos_list[1:]:
                totalDeVotos = totalDeVotos + int(voto)


        cargo_atual = CARGO
        candidatos = lista[0].split(";")
        if cargo_atual == 0:
            candidatos = candidatos[:10]
        elif cargo_atual == 1:
            candidatos = candidatos[:13]
 
        
        colocacao_list = []
        for i in range(len(candidatos)):
            nome = candidatos_legiveis[candidatos[i]]
            votosRecebidos = totalDeVotos_list[i]
            if totalDeVotos != 0:
                porcentagem = int((int(votosRecebidos)/totalDeVotos)*100)
            else:
                porcentagem = 0
            colocacao_list.append((nome,porcentagem,votosRecebidos))
            
        colocacao_list.sort(key=lambda x: x[1], reverse=True)
        if CARGO == 0:
            resultadoSenador = open(caminho + "/data/candidatos/votos/senador_resultado.txt",'w',encoding='utf-8')
            resultadoSenador.write("Nome;Porcentagem de Votos;Total de Votos Recebidos\n")
            for candidatoResultado in range(len(colocacao_list)):
                resultadoSenador.write(str(colocacao_list[candidatoResultado][0])+';'+ str(colocacao_list[candidatoResultado][1])+'%;'+str(colocacao_list[candidatoResultado][2])+"\n")
            resultadoSenador.close()
        elif CARGO == 1:
            resultadoPresidente = open(caminho +"/data/candidatos/votos/presidente_resultado.txt",'w',encoding='utf-8')
            resultadoPresidente.write("Nome;Porcentagem de Votos;Total de Votos Recebidos\n")
            for candidatoResultado in range(len(colocacao_list)):
  
                resultadoPresidente.write(str(colocacao_list[candidatoResultado][0])+';'+ str(colocacao_list[candidatoResultado][1])+'%;'+str(colocacao_list[candidatoResultado][2])+"\n")
            resultadoPresidente.close()
           
lista_candidatos(1)
initVotos()
resultado_votacao()