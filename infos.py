from graphics import *
    def candidato_info(vt):
        arquivo = open('.\\data\\candidatos\\candidatos.csv','r',encoding='utf-8')
        lista_candidatos = arquivo.read()
        lista_candidatos = lista_candidatos.split('\n')
        n_candidatos = arquivo.readlines()
        voto = vt
        
        n_eleitoral = []
        presidente = []
        vice = []
        partido = []
        foto = []
        votos = []
        qtd_votos = [0] * (len(n_candidatos)-1)
        for numero in lista_candidatos[1:]:
            n = numero.split(";")
            n_eleitoral.append(n[0])
            presidente.append(n[1])
            partido.append(n[2])
            vice.append(n[3])
            foto.append(n[4])
            
        
        if voto in n_eleitoral:
            for i in range(len(n_eleitoral)):
                if voto == n_eleitoral[i]:
                    presidente = presidente[i] 
                    partido = partido[i] 
                    vice = vice[i]
                    foto = foto[i] 
                    return presidente, partido, vice, foto
        else:
            return 'nulo'
        
    def tela_candidato(candidato_nome, candidato_partido, candidato_vice,foto): 
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
           
            candidato_nome_txt = candidato_nome
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
            
            tds_objts = [cargo_vice_txt,vice_foto,cargo_txt,candidato_foto,numero,nome,partido,vice,candidato_nome_obj,candidato_partido_obj,candidato_vice_obj]
            return tds_objts
            
        
        else:
            
            redraw_obj(obj)
            redraw(numero_errado)
            redraw(voto_nulo)
            
            tds_objts = [numero,numero_errado,voto_nulo]
            for i in tds_objts:
                obj_desenhados.append(i)
        
        
    def alinhamento(obj,txt,center_txt,x_align):
        for i in range(len(obj)):
            obj[i].setFace("courier")
            tamanho = len(txt[i])
            n_str = tamanho * 5
            l_point = center_txt - n_str
            l_align = abs(l_point - x_align)
            obj[i].move(l_align,0)
        
        