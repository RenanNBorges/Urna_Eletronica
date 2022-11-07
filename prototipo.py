
import time
import pressed
import objetos 
from graphics import *
from playsound import playsound

#Criando a Janela Principal
largura = 1000
altura = 700
objts_listas = []
def main():
    win = GraphWin("Urna Eletrônica por Renan Borges",largura,altura, autoflush=False)
    win.setBackground('white')
    # ------------------ Imagem da Urna ------------------
    urna_img = Image(Point(500,350),'.\\data\\img\\urna.gif')
    urna_img.draw(win)

    # ------------------ Construção da Tela ------------------
    
    tela = Rectangle(Point(120,213),Point(555,540))
    tela.draw(win)
    tela.setFill(color_rgb(50,50,50))
    
    def iniciando(r,g,b):
        # Objetos da Função
        ini_logo = Image(Point(337.5,340),'.\data\img\JE_logo.png')
        txt = Text(Point(335,450),"Iniciando...")
        bar = Rectangle(Point(170,470),Point(505,490))
        loading = Rectangle(Point(170,470),Point(170,490))
        txt2 = Text(Point(335,450),"Aperte confirmar")
        iniciando_objts = [ini_logo,txt,txt2,bar,loading]

        for i in range(41): #Animação de ligar tela
            if r == 250:
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
        objts_listas.append(iniciando_objts)
        return True


    telaAtual = -1
    while True:
        click = win.getMouse()
        if click != None and telaAtual == -1:
            telaAtual = 0
            ligado = iniciando(50,50,50) 
        elif ligado == True and pressed.confirma(click) != None:
            objetos.apagar(objts_listas[telaAtual],win)

    win.close()

main()