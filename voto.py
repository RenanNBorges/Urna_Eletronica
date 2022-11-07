from graphics import *
import telas

def conferir(lista):
    num_e = n_eleitoral 
    num = lista[0]
    for i in range(1,len(lista)):
        num += lista[i]
        if num in num_e:
            return num
        else:
            return 'nulo'

def todas_info(candidatos_arquivo):
    with open(candidatos_arquivo,'r',encoding='utf-8') as arquivo:
        lista_candidatos = arquivo.read()
        lista_candidatos = lista_candidatos.split('\n')
        n_candidatos = arquivo.readlines()
        qtd_votos = [0] * (len(n_candidatos)-1)
        for numero in lista_candidatos[1:]:
            n = numero.split(";")
            n_eleitoral.append(n[0])
            cargo.append(n[1])
            cargo_vice.append(n[2])
            nome_candidato.append(n[3])
            partido.append(n[4])
            vice.append(n[5])
            foto.append(n[6])
        return n_eleitoral,cargo,cargo_vice, nome_candidato, partido, vice, foto

def info_candidato(numero):
    n_eleitoral, cargo, cargo_vice, nome_candidato, partido, vice, foto = todas_info(lista_arquivos[0])
    for i in range(len(n_eleitoral)):
        if numero == n_eleitoral[i]:
            n_eleitoral = n_eleitoral[i]
            cargo = cargo[i]
            cargo_vice = cargo_vice[i]
            nome_candidato = nome_candidato[i] 
            partido = partido[i] 
            vice = vice[i]
            foto = foto[i] 
            return n_eleitoral,cargo,cargo_vice, nome_candidato, partido, vice, foto

lista_arquivos = ['.\\data\\candidatos\\presidente.csv']
n_eleitoral = []
nome_candidato = []
cargo = []
cargo_vice = []
vice = []
partido = []
foto = []
votos = []
n_eleitoral,cargo,cargo_vice, nome_candidato, partido, vice, foto = todas_info(lista_arquivos[0])

if __name__ == '__main__':
        

    a = ["1","3"]


    

    print(n_eleitoral)
    conferir(a)