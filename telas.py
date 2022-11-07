from graphics import *
import objetos
import voto
def iniciando(janela):
        txt = Text(Point(335,380),"Iniciando")
        bar = Rectangle(Point(170,400-10),Point(505,400+10))
        bar.draw(janela)
        txt.draw(janela)
        objt = [txt,bar]
        for i in range(1,101):
            
            loading = Rectangle(Point(170,400-10),Point(170+(3.35*i),400+10))
            loading.setFill('green')
            update()
            time.sleep(0.1)
            loading.draw(janela)
            objt.append(loading)
        txt.undraw()
        txt2 = Text(Point(335,380),"Aperte confirmar")
        txt2.draw(janela)
        objt.append(txt2)
        
        return True

    

def alinhamento(obj,txt,center_txt,x_align):
    for i in range(len(obj)):
        obj[i].setFace("courier")
        tamanho = len(txt[i])
        n_str = tamanho * 5
        l_point = center_txt - n_str
        l_align = abs(l_point - x_align)
        obj[i].move(l_align,0)

def digt_box(cargo):
    cargos = {'Presidente':2,'Senador':3,'Deputado Federal':4,'Deputado Estadual':5}
    for i in range(cargos[cargo]-1):
        box_digt = box[i].clone()
        box_digt.move(28,0)
        p1 = box_digt.getP1()
        p2 = box_digt.getP2()
        x1 = p1.getX()
        y1 = p1.getY()
        center = Point(x1 + 13,y1 + 16.5)
        box_center.append(center)
        box.append(box_digt)
    return box_center, box

def presidente_display():
    cargo = 'Presidente'
    cargo_txt = Text(Point(290,273),cargo)
    cargo_txt.setSize(18)
    cargo_txt.setFace("arial")
    box_center, box = digt_box(cargo)
    return cargo_txt,box_center, box

def senador_display():
    cargo = 'Senador'
    cargo_txt = Text(Point(290,273),cargo)
    cargo_txt.setSize(18)
    cargo_txt.setFace("arial")
    box_center, box = digt_box(cargo)
    return cargo_txt,box_center, box
# ------------- Layout Voto Display  --------------
def votoPara(): # Display "SEU VOTO PARA"
    seu_voto_para = Text(Point(190,233),"SEU VOTO PARA")
    return seu_voto_para
    
def rodape(): # Display Informações do rodapé
    corrige = Text(Point(263,527),"CORRIGE para REINICIAR este voto")
    corrige.setSize(10)
    confirmar = Text(Point(260,511),"CONFIRMA para CONFIRMAR este voto")
    confirmar.setSize(10)
    aperte = Text(Point(171,495),"Aperta a tecla:")
    aperte.setSize(10)
    line = Rectangle(Point(120,481),Point(555,481))
    line.setFill('black')
    rodape_obj = [line,aperte,confirmar, corrige]
    return rodape_obj

def votoBranco():
    branco_txt = Text(Point(337.5,376.5),"VOTO EM BRANCO")
    branco_txt.setSize(27)
    tela_branco = rodape()
    tela_branco.append(vt_para)
    tela_branco.append(branco_txt)
    return tela_branco

def votoNulo():
    numero = Text(Point(120+15,213+105),"Número:")
    numero_errado = Text(Point(120+93,213+135),"NÚMERO ERRADO")
    voto_nulo = Text(Point(120+240,213+220),"VOTO NULO")
    tela_nulo = rodape()
    obj = [numero]
    obj_txt = ["Número:"]
    numero_errado.setSize(15)
    voto_nulo.setSize(30)
    alinhamento(obj,obj_txt,120+15,120 + 6)
    tela_nulo.append(voto_nulo)
    tela_nulo.append(numero_errado)
    tela_nulo.append(numero)
    return tela_nulo

def candidato(candidato,cargo, cargo_vice, candidato_partido, candidato_vice, foto):
    candidato_foto = Image(Point(555-44.5,213+62),foto)
    vice_foto = Image(Point(555-35,213+235),'.\\data\\img\\candidatos\\vice-presidente\\12.png')
    cargo_txt = Text(Point(555-44.5,213+140),cargo)
    cargo_txt.setSize(11)
    cargo_vice_txt = Text(Point(555-35,213+290),cargo_vice)
    cargo_vice_txt.setSize(6)
    
    numero_txt = "Número:"
    nome_txt = "Nome:"
    partido_txt = "Partido:"
    vice_txt = "Vice:"
    
    numero = Text(Point(135,213+105),numero_txt)
    nome = Text(Point(135,213+135),nome_txt)
    partido = Text(Point(135,213+165),partido_txt)
    vice = Text(Point(135,213+205),vice_txt)
    
    candidato_nome_txt = candidato
    candidato_partido_txt = candidato_partido
    candidato_vice_txt = candidato_vice
    
    candidato_nome_obj = Text(Point(135,213+135),candidato_nome_txt)
    candidato_partido_obj = Text(Point(135,213+165),candidato_partido_txt)
    candidato_vice_obj = Text(Point(135,213+205),candidato_vice_txt)
    
    objts = [numero,nome,partido,vice]
    objts_txt = [numero_txt,nome_txt,partido_txt,vice_txt]
    
    candidato_info = [candidato_nome_obj,candidato_partido_obj,candidato_vice_obj]
    candidato_txt = [candidato_nome_txt,candidato_partido_txt,candidato_vice_txt]
    
    alinhamento(objts,objts_txt,135,126)
    alinhamento(candidato_info,candidato_txt,135,240)
    line,aperte,confirmar, corrige = rodape()
    tds_objts = [line,aperte,confirmar, corrige,cargo_vice_txt,vice_foto,cargo_txt,candidato_foto,numero,nome,partido,vice,candidato_nome_obj,candidato_partido_obj,candidato_vice_obj]
    return tds_objts


    

vt_para = votoPara() 
emVoto = rodape()
emVoto.append(vt_para)

box = []
box_center = []
box_digt = Rectangle(Point(240,298),Point(266,331))
center = Point(253,314.5)
box_center.append(center)
box.append(box_digt)
