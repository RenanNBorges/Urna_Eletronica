from graphics import *
def __main__():
    win_x = 1000
    win_y = 700
    win = GraphWin("Urna Eletrônica",win_x,win_y, autoflush=False)
    win.setBackground('white')
    
    # -------------- Layout da Urna --------------
    urna_x = win_x/2
    urna_y = win_y/2
    urna_img = Image(Point(urna_x,urna_y),"urna.png")
    urna_img.draw(win)
    
    x1 = 50
    x2 = 45
    x3 = win_x - 45
    x4 = win_x - 50
    
    y1 = 183
    y2 = 580.02
   
    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    p3 = Point(x3,y2)
    p4 = Point(x4,y1)
    
    urna_l = Polygon(p1,p2,p3,p4)
    urna_l.draw(win)
    # -------------- Tela Layout  --------------
    tela_x1 = x1 + 70
    tela_y1 = y1 + 30
    
    tela_x2 = tela_x1 + 435
    tela_y2 = tela_y1 + 327
    
    tela = Rectangle(Point(tela_x1,tela_y1),Point(tela_x2,tela_y2))
    tela.draw(win)
    tela.setFill('white')
    
    # -------------- Botao --------------
    b_x1 = tela_x2 + 65
    b_y1 = tela_y1 + 51
    
    b_x2 = b_x1 + 272
    b_y2 = b_y1 + 290
    
    botoes_layout = Rectangle(Point(b_x1,b_y1),Point(b_x2,b_y2))
    botoes_layout.draw(win)
    
    
    def teclas():
    # -------------- Tecla 1 --------------
        tecla1_x1 = b_x1 + 50
        tecla1_y1 = b_y1 + 23
    
        tecla1_x2 = b_x1 + 98
        tecla1_y2 = tecla1_y1 + 33
        tecla_1 = Rectangle(Point(tecla1_x1,tecla1_y1),Point(tecla1_x2,tecla1_y2))
        tecla_1.draw(win)
        
    # -------------- Tecla 2 --------------
        
        tecla2_x1 = tecla1_x2 + 18
        tecla2_y1 = b_y1 + 23
    
        tecla2_x2 = tecla2_x1 + 45
        tecla2_y2 = tecla2_y1 + 33
        tecla_2 = Rectangle(Point(tecla2_x1,tecla2_y1),Point(tecla2_x2,tecla2_y2))
        tecla_2.draw(win)
        
    # -------------- Tecla 3 --------------
        
        tecla3_x1 = tecla2_x2 + 18
        tecla3_y1 = b_y1 + 23
    
        tecla3_x2 = tecla3_x1 + 47
        tecla3_y2 = tecla3_y1 + 33
        tecla_3 = Rectangle(Point(tecla3_x1,tecla3_y1),Point(tecla3_x2,tecla3_y2))
        tecla_3.draw(win)
        
    # -------------- Tecla 4 --------------
        
        tecla4_x1 = b_x1 + 50
        tecla4_y1 = tecla1_y2 + 19
    
        tecla4_x2 = b_x1 + 98
        tecla4_y2 = tecla4_y1 + 33
        tecla_4 = Rectangle(Point(tecla4_x1,tecla4_y1),Point(tecla4_x2,tecla4_y2))
        tecla_4.draw(win)
        
    # -------------- Tecla 5 --------------
        
        tecla5_x1 = tecla4_x2 + 18
        tecla5_y1 = tecla2_y2 + 19
    
        tecla5_x2 = tecla5_x1 + 45
        tecla5_y2 = tecla5_y1 + 33
        tecla_5 = Rectangle(Point(tecla5_x1,tecla5_y1),Point(tecla5_x2,tecla5_y2))
        tecla_5.draw(win)
        
    # -------------- Tecla 6 --------------
        
        tecla6_x1 = tecla5_x2 + 18
        tecla6_y1 = tecla2_y2 + 19
    
        tecla6_x2 = tecla6_x1 + 47
        tecla6_y2 = tecla6_y1 + 33
        tecla_6 = Rectangle(Point(tecla6_x1,tecla6_y1),Point(tecla6_x2,tecla6_y2))
        tecla_6.draw(win)
        
    # -------------- Tecla 7 --------------
        
        tecla7_x1 = b_x1 + 51
        tecla7_y1 = tecla5_y2 + 21
        
        tecla7_x2 = b_x1 + 98
        tecla7_y2 = tecla7_y1 + 33
        tecla_7 = Rectangle(Point(tecla7_x1,tecla7_y1),Point(tecla7_x2,tecla7_y2))
        tecla_7.draw(win)
        
    # -------------- Tecla 8 --------------
        tecla8_x1 = tecla7_x2 + 18
        tecla8_y1 = tecla4_y2 + 21
        
        tecla8_x2 = tecla8_x1 + 46
        tecla8_y2 = tecla8_y1 + 33
        tecla_8 = Rectangle(Point(tecla8_x1,tecla8_y1),Point(tecla8_x2,tecla8_y2))
        tecla_8.draw(win)
        
    # -------------- Tecla 9 --------------
        tecla9_x1 = tecla8_x2 + 18
        tecla9_y1 = tecla4_y2 + 21
        
        tecla9_x2 = tecla9_x1 + 47
        tecla9_y2 = tecla9_y1 + 33
        tecla_9 = Rectangle(Point(tecla9_x1,tecla9_y1),Point(tecla9_x2,tecla9_y2))
        tecla_9.draw(win)
    # -------------- Tecla 0 --------------
        tecla0_x1 = tecla7_x2 + 18
        tecla0_y1 = tecla7_y2 + 21
        
        tecla0_x2 = tecla0_x1 + 46
        tecla0_y2 = tecla0_y1 + 33
        tecla_0 = Rectangle(Point(tecla0_x1,tecla0_y1),Point(tecla0_x2,tecla0_y2))
        tecla_0.draw(win)
        
    # -------------- Tecla Branco --------------
        teclaBranco_x1 = b_x1 + 17
        teclaBranco_y1 = tecla0_y2 + 19
        
        teclaBranco_x2 = teclaBranco_x1 + 70
        teclaBranco_y2 = teclaBranco_y1 + 36
        tecla_Branco = Rectangle(Point(teclaBranco_x1,teclaBranco_y1),Point(teclaBranco_x2,teclaBranco_y2))
        tecla_Branco.draw(win)
        
    # -------------- Tecla Corrige --------------
        teclaCorrige_x1 = teclaBranco_x2 + 17
        teclaCorrige_y1 = tecla0_y2 + 20
        
        teclaCorrige_x2 = teclaCorrige_x1 + 68
        teclaCorrige_y2 = teclaCorrige_y1 + 35
        tecla_Corrige = Rectangle(Point(teclaCorrige_x1,teclaCorrige_y1),Point(teclaCorrige_x2,teclaCorrige_y2))
        tecla_Corrige.draw(win)
        
    # -------------- Tecla Confirma --------------
        teclaConfirma_x1 = teclaCorrige_x2 + 16
        teclaConfirma_y1 = tecla0_y2 + 10
        
        teclaConfirma_x2 = teclaConfirma_x1 + 70
        teclaConfirma_y2 = teclaConfirma_y1 + 45
        tecla_Confirma = Rectangle(Point(teclaConfirma_x1,teclaConfirma_y1),Point(teclaConfirma_x2,teclaConfirma_y2))
        tecla_Confirma.draw(win)
        
    # -------------- Retorno da Função --------------
        return tecla_1,tecla_2, tecla_3, tecla_4, tecla_5, tecla_6, tecla_7, tecla_8, tecla_9, tecla_0, tecla_Branco, tecla_Corrige, tecla_Confirma
    # -------------- Digito Retangulo  --------------
    def qts_retangulos(cargo):
        cargos = {'Presidente':2,'Senador':3,'Deputado Federal':4,'Deputado Estadual':5}
    
        r_digtx1 = tela_x1 + 70
        r_digtx2 = r_digtx1 + 30
    
        r_digty1 = tela_y1 + 85
        r_digty2 = r_digty1 + 33
        dist_rx = r_digtx2 - r_digtx1
        
        r_digt = Rectangle(Point(r_digtx1,r_digty1),Point(r_digtx2,r_digty2))
        r_digt.draw(win)
        
        
        retangulos = []
        r_center = []
        centerx = r_digtx1 +((r_digtx2 - r_digtx1)/2)
        centery = r_digty1 +((r_digty2 - r_digty1)/2)
        center = Point(centerx,centery)
        r_center.append(center)
        retangulos.append(r_digt)
        
        
        for i in range(cargos[cargo]-1):
            r_digt = retangulos[i].clone()
            
            r_digt.move(dist_rx + 2,0)
            
            r_digt.draw(win)
            
            
            
            p1 = r_digt.getP1()
            p2 = r_digt.getP2()
            
            r_digtx1 = p1.getX()
            r_digtx2 = p2.getX()
            
            r_digty1 = p1.getY()
            r_digty2 = p2.getY()
            
            centerx = r_digtx1 +((r_digtx2 - r_digtx1)/2)
            centery = r_digty1 +((r_digty2 - r_digty1)/2)
            center = Point(centerx,centery)
            r_center.append(center)
            retangulos.append(r_digt)
        return r_center, retangulos
    
    # -------------- Detectar Tecla --------------
    def press(click, tecla):
        ll = tecla.getP1()
        ur = tecla.getP2()
        
        return ll.getX() < click.getX() < ur.getX() and ll.getY() < click.getY() < ur.getY()
    
    tecla_1,tecla_2, tecla_3, tecla_4, tecla_5, tecla_6, tecla_7, tecla_8, tecla_9, tecla_0, tecla_Branco, tecla_Corrige, tecla_Confirma = teclas()
    
    def digt():
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
            elif press(click, tecla_Branco):
                return "Branco"
            elif press(click, tecla_Corrige):
                return "Corrige"
            elif press(click, tecla_Confirma):
                return "Confirma"
    # --------------  --------------
    def voto_valido(digito_1,digito_2,arquivo):
        
        digt1 = digito_1
        digt2 = digito_2
        print(digt1,digt2)
        
        arquivo = open(arquivo,'r',encoding='utf-8')
        lista_candidatos = arquivo.read()
        lista_candidatos = lista_candidatos.split('\n')
        
        voto = digt1 + digt2
    
        n_eleitoral = []
        for numero in lista_candidatos[1:]:
                n = numero.split(";")
                n_eleitoral.append(n[0])
                if voto in n_eleitoral:
                    return voto
        return print("Voto Nulo")
    # --------------  --------------
    def vt_valido():
            digt1 = digt()
            digt2 = digt()
            voto = voto_valido(digt1,digt2,'candidatos.csv')
            return voto
    # --------------  --------------
    
    # --------------  --------------
    def tela_digito(digito,box_center):
        center = box_center
        digit = Text(center,digito)
        digit.draw(win)
        return digito
    
    # -------------- Voto --------------
    digitos = []
    def voto():
        voto = digitos[0]
        for i in range(1,len(lista)):
            voto = voto + digitos[i]
        return print(voto)
    
    # -------------- --------------
    # -------------- Tela Layout  --------------
    def cargo_display(cargo):
        cargos = ['Senador','Presidente']
        x = tela_x1 + 170
        y = tela_y1 + 60
        cargo_txt = Text(Point(x,y),cargos[cargo])
        
        cargo_txt.setSize(18)
        cargo_txt.setFace("arial")
        cargo_txt.draw(win)
        return cargos[cargo], cargo_txt
    
    # -------------- Apagar Objeto  --------------
    def undraw(objeto):
        objeto.undraw()
        
    def zerar():
        for i in range(len(objetos)):
            undraw(objetos[i])
        undraw(cargo_txt)
    
    # -------------- --------------
    def seu_voto_para():
        x = tela_x1 + 70
        y = tela_y1 + 20
        seu_voto_para = Text(Point(x,y),"SEU VOTO PARA")
        seu_voto_para.draw(win)
        return seu_voto_para
    
    seu_voto_para()
    # -------------- --------------
    cargo, cargo_txt = cargo_display(1)
    lista, objetos = qts_retangulos(cargo)
    for i in range(len(lista)):
        digitos.append(tela_digito(digt(),lista[i]))
    voto()
    # -------------- --------------
    
    win.getMouse()
    win.close()
    
__main__()