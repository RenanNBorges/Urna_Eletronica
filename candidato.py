import objetos
from graphics import *
pathCargoFile = ['.\data\candidatos\senador.csv','.\data\candidatos\presidente.csv',]
n_eleitoral_list = []
n_eleitoral = [0]
nome_list = []
vice_list = []
partido_list = []
foto_list = []

def cargoFile(cargo):
    print(pathCargoFile[cargo-1])
    return pathCargoFile[cargo-1]
def reset_listas():
    objetos.del_lista(n_eleitoral_list)
    objetos.del_lista(nome_list)
    objetos.del_lista(partido_list)
    objetos.del_lista(vice_list)
    objetos.del_lista(foto_list)

def lista_candidatos(telaAtual):
        arquivo = open(cargoFile(telaAtual),'r',encoding='utf-8')
        listaCandidatos = arquivo.read()
        print(listaCandidatos)
        listaCandidatos = listaCandidatos.split('\n')
        print(listaCandidatos)
        arquivo.close()

        for candidatos in listaCandidatos[1:]:
            print(candidatos)
            candidato = candidatos.split(";")
            n_eleitoral_list.append(candidato[0])
            nome_list.append(candidato[1])
            partido_list.append(candidato[2])
            vice_list.append(candidato[3])
            foto_list.append(candidato[4])
            print(n_eleitoral_list)
        
        return n_eleitoral_list

def valido(VOTO,telaAtual):
    
    if telaAtual != 3:
        n_eleitoral[0] = lista_candidatos(telaAtual)
        for i in range(len(n_eleitoral[0])):
            print('Teste de numero eleitoral',n_eleitoral[0][i])
            if VOTO == n_eleitoral[0][i]:
                return "valido"
            
        reset_listas()
        return "nulo"
    else:
        return 0
    
def infos(VOTO):
    print(n_eleitoral[0])
    for i in range(len(n_eleitoral[0])):
        
        if VOTO == n_eleitoral[0][i]:
            
            nome_candidato = nome_list[i] 
            partido_candidato = partido_list[i] 
            vice_candidato = vice_list[i]
            foto_candidato = foto_list[i] 
            print(nome_candidato, partido_candidato,vice_candidato,foto_candidato)
            return nome_candidato, partido_candidato,vice_candidato,foto_candidato

def display(voto,telaAtual):
    nome, partido,vice,foto = infos(voto)
    cargo = {1:"Senador",2:"Presidente"}
    cargoVice = {1:"Suplente",2:"Vice-Presidente"}
    foto_obj = Image(Point(555-44.5,213+62),foto)
    cargo_txt = Text(Point(555-44.5,213+140),cargo[telaAtual])
    cargo_txt.setSize(11)
    cargo_vice_txt = Text(Point(555-35,213+290),cargoVice[telaAtual])
    cargo_vice_txt.setSize(6)
    nome_obj = Text(Point(135,213+135),nome)
    partido_obj = Text(Point(135,213+165),partido)
    vice_obj = Text(Point(135,213+205),vice)
    candidato_display = [foto_obj,cargo_txt,cargo_vice_txt,nome_obj,partido_obj,vice_obj]
    reset_listas()
    return candidato_display

    
