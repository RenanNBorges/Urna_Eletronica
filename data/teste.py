from graphics import *
def main():
    win = GraphWin("",200,200)
    r_digt = Rectangle(Point(50,70),Point(100,80))
    r_digt.draw(win)
        
    retangulos = []
    r_center = []
    center = r_digt.getCenter
    print(center)
main()