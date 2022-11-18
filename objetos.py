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

def alinhamento(obj,x_align):
    for i in obj:
        objtexto = i
        txt = objtexto.getText()
        point = objtexto.getAnchor()
        center_txt = point.getX()
        objtexto.setFace("courier")
        tamanho = len(txt)
        n_str = tamanho * 5
        l_point = center_txt - n_str
        l_align = abs(l_point - x_align)
        objtexto.move(l_align,0)
    