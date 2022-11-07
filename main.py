import time
import pressed
import telas
import objetos
import voto
from graphics import *
def __main__():
    win_x = 1000
    win_y = 700
    win = GraphWin("Urna Eletrônica",win_x,win_y, autoflush=False)
    win.setBackground('white')
    # -------------- Layout da Urna --------------
    urna_img = Image(Point(500,350),".\\data\\img\\urna.png")
    urna_img.draw(win)
    # -------------- Tela Layout  --------------
    tela = Rectangle(Point(120,213),Point(555,540))
    tela.draw(win)
    tela.setFill('white')
    # -------------- Digito Display --------------
    def draw_digito(digito,rectangle):
        center = rectangle
        numero = Text(center,digito)
        numeros_na_tela.append(numero)
        numero.draw(win)
        return numero

    def voto_tela(contador):
        global cargoTxt,box_center, box
        if contador == 1:
            cargoTxt,box_center, box = telas.presidente_display()
        elif contador == 0:
            cargoTxt,box_center, box = telas.senador_display()
        objetos.redraw_list(box,win)
        objetos.redraw(votoPara,win)
        objetos.redraw(cargoTxt,win)
        objetos.add_lista(obj_in_tela,box)
        return box_center, box
    
    def tecla_numerica(tecla,digt):
        num = draw_digito(tecla,box_center[digt])
        obj_in_tela.append(num)
        in_tela.append(num)
        digitos.append(tecla)
        objetos.add_lista(obj_in_tela,in_tela)
        digt += 1
        return digt
        

    # -------------- Funções de Display --------------  
    
    contador_geral = 0
    
    cont = 1
    in_tela = []
    digitos = []
    obj_in_tela = []
    digitos = []
    numeros_na_tela = []
    digt = 0
    votos_presidente = [0] * 12 
    votos_senador = [0] * 9
    
    obj_vtBranco = telas.votoBranco()
    votoPara = telas.votoPara()
    emVoto_txt = telas.emVoto
    
    branco_Obj = telas.votoBranco()
    
    num_tela = False
    ligado = False
    ativo = 0
    while contador_geral < 3:
        if ligado == False:
            ligado, objts = telas.iniciando(win)
            
            if ativo == 0:
                click = win.getMouse()
                ativo = pressed.corrige(click)
                objetos.apagar(objts,win)
                break

    if ligado == True: 
        box_center, box = voto_tela(contador_geral)
        branco = False
        while True:
           
            click = win.getMouse()
            a = pressed.tecla(click)
            b = pressed.branco(click)
            c = pressed.corrige(click)
            d = pressed.confirma(click)
            
            if a != None and digt < len(box_center) and ligado == True and branco == False:
                digt = tecla_numerica(a,digt)
                if digt == len(box_center):
                    num_voto = voto.conferir(digitos)
                    if num_voto != "nulo":
                        n_eleitoral,cargo,cargo_vice, nome_candidato, partido, vice, foto = voto.info_candidato(num_voto)
                        tela_infos = telas.candidato(nome_candidato,cargo,cargo_vice, partido, vice, foto)
                        objetos.add_lista(obj_in_tela,tela_infos)
                        objetos.redraw_list(tela_infos,win)
                        
                    else:
                        nulo = telas.votoNulo()
                        objetos.add_lista(obj_in_tela,nulo)
                        objetos.redraw_list(nulo,win)
                        num_voto = 0
                    
                num_tela = True
            elif (b != None) and (num_tela == False) and ligado == True:
                objetos.add_lista(obj_in_tela,branco_Obj)
                objetos.apagar(obj_in_tela,win)
                objetos.redraw_list(branco_Obj,win)
                branco = True
                num_voto = "0"
            elif c != None and ligado == True:
                votoPara.undraw()
                cargoTxt.undraw()
                objetos.apagar(obj_in_tela,win)
                for i in range(len(in_tela)):
                    del(in_tela[0])
                
                for i in range(len(digitos)):
                    del(digitos[0])
                digt = 0
                voto_tela(contador_geral)
                print('corrige',len(in_tela))
                num_tela = False
                branco = False
            elif d != None and digt == len(box_center) and ligado == True:
                lista_eleitoral = voto.todas_info('.\\data\\candidatos\\presidente.csv')
                for i in range(len(votos_presidente)-1):
                    if num_voto == lista_eleitoral[0][i]:
                        votos_presidente[i] = votos_presidente[i] + 1
                        print(votos_presidente)
                
                with open('.\\data\\candidatos\\voto_presidente.txt','w',encoding='utf-8') as voto_presi:
                    for i in votos_presidente:
                        texto =  str(i) + ' ' 
                        voto_presi.write(texto)
                votoPara.undraw()
                cargoTxt.undraw()
                objetos.apagar(obj_in_tela,win)
                contador_geral += 1
                for i in range(len(digitos)):
                    del(digitos[0])
                digt = 0
                voto_tela(contador_geral)
                
                
__main__() 