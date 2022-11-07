from graphics import *
def desenhar(objetos,janela):
    for i in range(len(objetos)):
        objetos[i].draw(janela)

def apagar(objetos,janela):
    for i in range(len(objetos)):
        objetos[i].undraw()

def redraw_list(lista_objetos,janela):
    apagar(lista_objetos,janela)
    desenhar(lista_objetos,janela)

def redraw(objeto,janela):
    objeto.undraw()
    objeto.draw(janela)

def na_tela(objTela,lista):
    for i in lista:
        objTela.append(i)
    return objTela
    