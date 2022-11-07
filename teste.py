import time
import teclas
from graphics import *
def main():
    win_x = 1000
    win_y = 700
    win = GraphWin("Urna Eletrônica",win_x,win_y, autoflush=False)
    win.setBackground("white")
    
    urna_x = 500
    urna_y = 350
    urna_img = Image(Point(urna_x,urna_y),".\\data\\img\\urna.gif")
    urna_img.draw(win)
    
    def press(click, tecla):
        ll = tecla.getP1()
        ur = tecla.getP2()
        return ll.getX() < click.getX() < ur.getX() and ll.getY() < click.getY() < ur.getY()
    tecla_1,tecla_2, tecla_3, tecla_4, tecla_5, tecla_6, tecla_7, tecla_8, tecla_9, tecla_0, tecla_Branco, tecla_Corrige, tecla_Confirma = teclas.botao()
    
    def tecla_num():
        while True:
            click = win.getMouse()
            if click is None:
                continue
            elif press(click, tecla_1):
                return "1"
            elif press(click, tecla_2):
                return "2"
            elif press(click, tecla_3):
                return "3"
            elif press(click, tecla_4):
                return "4"
            elif press(click, tecla_5):
                return "5"
            elif press(click, tecla_6):
                return "6"
            elif press(click, tecla_7):
                return "7"
            elif press(click, tecla_8):
                return "8"
            elif press(click, tecla_9):
                return "9"
            elif press(click, tecla_0):
                return "0"
    
    while True:
        win.getMouse()
        win.close()
    
main()