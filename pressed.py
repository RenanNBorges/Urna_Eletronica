from graphics import * 
def botao():
# -------------- Tecla 1 --------------
    tecla_1 = Rectangle(Point(670,287),Point(715,320))
# -------------- Tecla 2 --------------
    tecla_2 = Rectangle(Point(735,285),Point(780,320))
# -------------- Tecla 3 --------------
    tecla_3 = Rectangle(Point(800,285),Point(845,320))
# -------------- Tecla 4 --------------
    tecla_4 = Rectangle(Point(670,340),Point(715,375))
# -------------- Tecla 5 --------------
    tecla_5 = Rectangle(Point(735,340),Point(780,375))
# -------------- Tecla 6 --------------
    tecla_6 = Rectangle(Point(800,340),Point(845,375))
# -------------- Tecla 7 --------------
    tecla_7 = Rectangle(Point(670,395),Point(715,430))
# -------------- Tecla 8 --------------
    tecla_8 = Rectangle(Point(735,395),Point(780,430))
# -------------- Tecla 9 --------------
    tecla_9 = Rectangle(Point(800,392),Point(845,427))
# -------------- Tecla 0 --------------
    tecla_0 = Rectangle(Point(738,447),Point(783,483))
# -------------- Tecla Branco --------------
    tecla_Branco = Rectangle(Point(637,502),Point(707,538))
# -------------- Tecla Corrige --------------
    tecla_Corrige = Rectangle(Point(724,502),Point(792,537))
# -------------- Tecla Confirma --------------
    tecla_Confirma = Rectangle(Point(808,493),Point(878,538))
# -------------- Retorno da Função --------------
    return tecla_1,tecla_2, tecla_3, tecla_4, tecla_5, tecla_6, tecla_7, tecla_8, tecla_9, tecla_0, tecla_Branco, tecla_Corrige, tecla_Confirma

tecla_1,tecla_2, tecla_3, tecla_4, tecla_5, tecla_6, tecla_7, tecla_8, tecla_9, tecla_0, tecla_Branco, tecla_Corrige, tecla_Confirma = botao()

def area(click, tecla):
        if click is None:
            return 0
        else:
            ll = tecla.getP1()
            ur = tecla.getP2()
            return ll.getX() < click.getX() < ur.getX() and ll.getY() < click.getY() < ur.getY()

def tecla(click):
    if click is None:
        return 0 
    elif area(click, tecla_1):
        return "1"
    elif area(click, tecla_2):
        return "2"
    elif area(click, tecla_3):
        return "3"
    elif area(click, tecla_4):
        return "4"
    elif area(click, tecla_5):
        return "5"
    elif area(click, tecla_6):
        return "6"
    elif area(click, tecla_7):
        return "7"
    elif area(click, tecla_8):
        return "8"
    elif area(click, tecla_9):
        return "9"
    elif area(click, tecla_0):
        return "0"

def branco(click):
    if click is None:
        return 0
    elif area(click, tecla_Branco):
        return 1

def corrige(click):
    if click is None:
        return 0
    elif area(click, tecla_Corrige):
        return 1

def confirma(click):
    if click is None:
        return 0 
    elif area(click, tecla_Confirma):
        return 1