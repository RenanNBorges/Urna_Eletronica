import time
import objetos
import candidato
from pressed import *
from graphics import *
from playsound import playsound

#Criando a Janela Principal
largura = 1000
altura = 700

def main():
    win = GraphWin("Urna Eletrônica por Renan Borges",largura,altura, autoflush=False)
    win.setBackground('white')
    # ------------------ Imagem da Urna ------------------
    urna_img = Image(Point(500,350),'.\\data\\img\\urna.gif')
    urna_img.draw(win)

    # ------------------ Funções para Objetos Dinâmicos ------------------
    def qtd_box(cargo): # Cria as caixas que mostram os digitos
        box_digt = Rectangle(Point(240,298),Point(266,331))
        box = [box_digt]
        box_center = []
        for i in range(cargo):
            box_digt = box[i].clone()
            box_digt.move(28,0)
            box.append(box_digt)
        return box


    def boxCenter(boxLista): # Pegar as coordenadas do centro das caixas que mostram os digitos
        centerBoxList = []
        for i in boxLista:
            p1 = i.getP1()
            p2 = i.getP2()
            x1 = p1.getX()
            y1 = p1.getY()
            center = Point(x1 + 13,y1 + 16.5)
            centerBoxList.append(center)
        return centerBoxList
    # ------------------ Construção da Tela ------------------
    
    tela = Rectangle(Point(120,213),Point(555,540))
    tela.draw(win)
    tela.setFill(color_rgb(50,50,50))
    desligado = tela.clone()
    
    # ------------------ Tela de Iniciação ------------------
    def iniciando(r,g,b):
        # Objetos da Função
        ini_logo = Image(Point(337.5,340),'.\data\img\JE_logo.png')
        txt = Text(Point(335,450),"Iniciando...")
        bar = Rectangle(Point(170,470),Point(505,490))
        loading = Rectangle(Point(170,470),Point(170,490))
        txt2 = Text(Point(335,450),"Pronto")
        iniciando_objts = [ini_logo,txt,txt2,bar,loading]

        for i in range(42): #Animação de ligar tela
            if r == 255:
                ini_logo.draw(win)
                txt.draw(win)
            else:
                r += 5
                g += 5
                b += 5
                tela.setFill(color_rgb(r,g,b))
            update(60)
            
        bar.draw(win)
        playsound('iniciar.mp3')
        for i in range(1,106,5): # Animação "iniciando..."
            loading.undraw()
            loading = Rectangle(Point(170,470),Point(170+(3.35*i),490))
            loading.setFill('green')
            time.sleep(0.1)
            loading.draw(win)
            iniciando_objts.append(loading)
            update(60)
        txt.undraw()
        
        txt2.draw(win)
        objetos.na_tela(objetosNaTela,iniciando_objts)
        return True

    def fim():
        votouTxt = Text(Point(555-45,213+290),"VOTOU")
        votouTxt.setSize(20)
        votouTxt.setTextColor('grey')
        fimTxt = Text(Point(337.5,376.5),"FIM")
        fimTxt.setSize(36)
        
        txt = Text(Point(335,450),"Gravando...")
        bar = Rectangle(Point(170,470),Point(505,490))
        loading = Rectangle(Point(170,470),Point(170,490))
        fim_objts = [fimTxt,votouTxt,txt,bar,loading]

        txt.draw(win)
        bar.draw(win)
        for i in range(1,106,5): # Animação "iniciando..."
            loading.undraw()
            loading = Rectangle(Point(170,470),Point(170+(3.35*i),490))
            loading.setFill('green')
            time.sleep(0.1)
            loading.draw(win)
            fim_objts.append(loading)
            update(60)
        time.sleep(0.5)
        objetos.na_tela(objetosNaTela,fim_objts)
        reset_tela()
        fimTxt.draw(win)
        votouTxt.draw(win)
        objetos.na_tela(objetosNaTela,fim_objts)
        
        return 4
        
        

    #------------------ Tela Receber Voto ------------------
    def tela_cargo(cargo,box): #Mostra o CARGO e a quantidade correspondendende retangulos 
        cargo_display = Text(Point(290,273),cargo)
        cargo_display.setSize(18)
        cargo_display.setFace("arial")
        cargo_display.draw(win)
        votoPara.draw(win)
         
        recebe_objts = [cargo_display,votoPara]
        objetos.na_tela(recebe_objts,box)
        objetos.redraw_list(box,win)
        objetos.na_tela(objetosNaTela,recebe_objts)
        print('entrou no indice',len(objetosNaTela)-1)

    def num_tela(tecla,centerPoint,digito): #Desenha o número digitado na tela
        if tecla != None:
            numero = Text(centerPoint[digito[0]],tecla)
            digito[0] += 1
            numero.draw(win)
            voto_digitos.append(tecla)
            digitoInTela.append(numero)
            objetosNaTela.append(numero)
        else:
            return 0
    def reset_digtos(): # Apaga os números na tela
        objetos.apagar(digitoInTela,win)
        objetos.del_lista(voto_digitos)
        objetos.del_lista(digitoInTela)
        digito[0] = 0
        preenchido[0] = False


    def reset_tela(): # Apaga todos os objetos na tela, usado pra troca de tela
        objetos.apagar(objetosNaTela,win)
        reset_digtos()
        objetos.del_lista(objetosNaTela)

    def teclas(): # Verifica quais teclas foram pressionadas
            if telaAtual[0] == 0: # Verificando se está em uma tela que use as teclas
                return 0
            else:
                if tecla(click) != None and digito[0] < len(txtCenter): # Tecla para os números, coloca eles na tela
                    num_tela(tecla(click),txtCenter,digito)
                
                elif branco(click) != None and len(digitoInTela) == 0: # Tecla voto branco
                    reset_tela()
                    objetos.redraw_list(branco_objts,win)
                    objetos.na_tela(objetosNaTela,branco_objts)
                    for i in range((len(box))):
                        voto_digitos.append("Nda")
                    
                elif corrige(click) != None and digitoInTela != 0: # Tecla de Corrigir, apaga tudo e volta pra tela de receber voto do cargo atual
                    reset_tela()
                    tela_cargo(cargo,box)
                elif confirma(click) != None and len(voto_digitos) == len(box): # Tecla Confirmar, encerra a tela de voto atual e vai pra próxima
                    reset_tela()
                    statusVoto[0] = "Recebido"
                    telaAtual[0] += 1 

    def testar_voto(): #Testa se os números inseridos são de um candidato
        if telaAtual[0] == 0 or len(digitoInTela) == 0 or digitoInTela[0] == "Nda":
            return 0
        else:
            if len(digitoInTela) == len(box) and preenchido[0] == False:
                votoRecebido_objts = [votoPara,numeroTxt,partidoTxt,nomeTxt,viceTxt]
                preenchido[0] = True
                voto =  voto_digitos[0]
                for i in voto_digitos[1:]:
                    voto += i

                print('voto=',voto)
                if candidato.valido(voto,telaAtual[0]) == "valido":
                    info_eleitoral = []
                    info_eleitoral = candidato.display(voto,telaAtual[0])
                    objetos.alinhamento(info_eleitoral[3:],240)
                    objetos.redraw_list(info_eleitoral,win)
                    objetos.redraw_list(votoRecebido_objts,win)
                    objetos.redraw_list(rodape_objts,win)
                    objetos.na_tela(votoRecebido_objts,info_eleitoral)
                    objetos.na_tela(objetosNaTela,rodape_objts)
                    objetos.na_tela(objetosNaTela,votoRecebido_objts)
                
                elif candidato.valido(voto,telaAtual[0]) == "nulo":
                    objetos.redraw_list(rodape_objts,win)
                    objetos.redraw_list(nulo_objts,win)
                    objetos.na_tela(objetosNaTela,nulo_objts)
                    objetos.na_tela(objetosNaTela,rodape_objts)            
    # -----------------------
    # Listas de Objetos da Tela
    objetosNaTela = []
    digitoInTela = []
    #Informações do Rodape
    votoPara = Text(Point(190,233),"SEU VOTO PARA")
    corrige_rodape = Text(Point(263,527),"CORRIGE para REINICIAR este voto")
    corrige_rodape.setSize(10)
    confirmar_rodape = Text(Point(260,511),"CONFIRMA para CONFIRMAR este voto")
    confirmar_rodape.setSize(10)
    aperte_rodape = Text(Point(171,495),"Aperta a tecla:")
    aperte_rodape.setSize(10)
    line_rodape = Rectangle(Point(120,481),Point(555,481))
    line_rodape.setFill('black')
    rodape_objts = [line_rodape,corrige_rodape,confirmar_rodape,aperte_rodape]
    # Tela de Voto
    numeroTxt = Text(Point(135,213+105),"Número:")
    nomeTxt = Text(Point(135,213+135),"Nome:")
    partidoTxt = Text(Point(135,213+165),"Partido:")
    viceTxt = Text(Point(135,213+205),"Vice:")
    suplenteTxt = Text(Point(135,213+205),"1º Suplente:")
    tela_voto_txt = [numeroTxt,nomeTxt,partidoTxt,viceTxt,suplenteTxt]
    objetos.alinhamento(tela_voto_txt,126)
    # Tela Voto Branco
    brancoTxt = Text(Point(337.5,376.5),"VOTO EM BRANCO")
    brancoTxt.setSize(27)
    branco_objts = [votoPara,brancoTxt]
    objetos.na_tela(branco_objts,rodape_objts)
    # Tela Voto Nulo
    numero_errado = Text(Point(120+93,213+135),"NÚMERO ERRADO")
    voto_nulo = Text(Point(120+240,213+220),"VOTO NULO")
    numero_errado.setSize(15)
    voto_nulo.setSize(30)
    nulo_objts = [numeroTxt,votoPara,numero_errado,voto_nulo]
    # Botões
    iniciarImg = Image(Point(100,640),".\\data\\img\\buttons\\start.gif")
    encerrarImg = Image(Point(200,640),".\\data\\img\\buttons\\stop.gif")
    iniciarImg.draw(win)
    encerrarImg.draw(win)
    iniciar = Rectangle(Point(60,600),Point(140,640))
    encerrar = Rectangle(Point(160,600),Point(240,640))
    # Listas 
    telaAtual = [-1] # Contador para saber qual tela mostrar
    digito = [0] # Contador de digitos
    preenchido = [False] #Contador para saber se já foi preenchidos todos os digitos na tela e evitar loop de verificar voto
    voto_digitos = [] # Lista o para armazenar o voto
    statusVoto = ["Não Recebido"] # Saber se o voto foi armazenado
    telas = ['Iniciar','Senador','Presidente','Fim','Chave Para Encerrar','Tela Desligada'] #Lista de telas
    n_cargo = {"Senador":2,"Presidente":1,"Deputado Federal":4,"Chave Para Encerrar":4} #Dicionario que indica a quantidade de retangulos na tela
    txtCenter = [] # Lista que armazena as coordenadas xy do centro de cada retangulo para colocar os números
    in_tela = False
    ligado = False
    box = None
    r = 255
    g = 255
    b = 255
    tempo = 0
    while True:
        click = win.checkMouse()
        cargo = telas[telaAtual[0]]

        if area(click,iniciar) == True and ligado == False:
            objetos.apagar(objetosNaTela,win)
            ligado = iniciando(50,50,50)
            telaAtual[0] = 1

        elif ligado == True and in_tela == False and telaAtual[0] == 1: #Tela Senador
            objetos.apagar(objetosNaTela,win)
            box = qtd_box(n_cargo[cargo])
            tela_cargo(cargo,box)
            txtCenter = boxCenter(box)
            in_tela = True

        elif ligado == True and statusVoto[0] == "Recebido" and telaAtual[0] == 2: #Tela Presidente
            statusVoto[0] = "Não Recebido"
            box = qtd_box(n_cargo[cargo])
            tela_cargo(cargo,box)
            txtCenter = boxCenter(box)

        elif ligado == True and statusVoto[0] == "Recebido" and telaAtual[0] == 3:
            reset_tela()
            statusVoto[0] = "Não Recebido"
            telaAtual[0] == fim()
            telaAtual[0] = 4
            

        elif ligado == True != None and telaAtual[0] == 4:
            playsound('Fim.mp3')
            time.sleep(5)
            reset_tela()
            for i in range(42): #Animação de ligar tela
                r = r - 5
                g = g - 5
                b = b - 5
                tela.setFill(color_rgb(r,g,b))
            ligado = False
            in_tela = False
            telaAtual[0] = -1
    
        if click != None and ligado == True and telaAtual[0] != 3:
            teclas()
            testar_voto()

        if area(click,encerrar):
            break
        update(30) 

    win.close()

main()