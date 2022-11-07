def voto_pres(dig1,dig2):
    with open('.\\candidatos\\candidatos.csv','r',encoding='utf-8') as arquivo:
        aa = open("aa.txt","w+")
        lista_candidatos = arquivo.read()
        lista_candidatos = lista_candidatos.split('\n')
        
        voto = "12"
        
        n_eleitoral = []
        presidente = []
        vice = []
        partido = []
        foto = []
        votos = []
        qtd_votos = [0] * 11
        for numero in lista_candidatos[1:]:
            n = numero.split(";")
            n_eleitoral.append(n[0])
            presidente.append(n[1])
            partido.append(n[2])
            vice.append(n[3])
            foto.append(n[4])
            votos.append(n[5])
        
        if voto in n_eleitoral:
            print("true")
            for i in range(len(n_eleitoral)):
                if voto == n_eleitoral[i]:
                    qtd_votos[i] += 1
                    print(n_eleitoral[i],presidente[i],partido[i],vice[i],foto[i],qtd_votos[i])
                    break
                elif voto == "00":
                    qtd_votos[-1] += 1
                else:
                    continue
        else:
            qtd_votos[-1] += 1
        a = ";"
        for i in qtd_votos:
            a =  str(i) + ' ' 
            aa.write(a)
        aa.close()
        print(qtd_votos)

voto_pres(1,2)