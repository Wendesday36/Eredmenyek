# megoldas
def eredmeny(jatekoskatya: [int], gepkartya: [int]):
    allapot = 0
    if osszeg(jatekoskatya) > 21:
        allapot = "jatekos vesztett"
    elif osszeg(gepkartya) > 21:
        allapot = "gép vesztett"
    return allapot



def osszeg(kartyak: [int]):
    pontok: int = 0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok


#tesztesetek


def teszt_esetek():
    jatekos_vesztett()
    jatekos_vesztett_kevesebb()
    jatekos_vesztett_tobb()
    gep_vesztett()
    gep_vesztett_tobblap()
    gep_vesztett_kevesebblap()
    dontetlen_gep()
    dontetlen_jatekos()
def jatekos_vesztett():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "jatekos veszett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")






def jatekos_vesztett_kevesebb():
    jatekos = [10, 9]
    gep = [10, 10, 1]
    vart_eredmeny = "jatekos veszett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett_kevesebb teszt sikeres")
    else:
        print("a jatekos_vesztett_kevesebb teszt megbukott")



def jatekos_vesztett_tobb():
    jatekos = [10, 10, 1]
    gep = [10, 10]
    vart_eredmeny = "jatekos veszett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett_tobb teszt sikeres")
    else:
        print("a jatekos_vesztett_tobb teszt megbukott")




def gep_vesztett():
    jatekos = [10, 10, 2]
    gep = [10, 10]
    vart_eredmeny = "gép veszett"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_vesztett teszt sikeres")
    else:
        print("a gep_vesztett teszt megbukott")


def gep_vesztett_kevesebblap():
    jatekos = [10, 10]
    gep = [10, 8, 4]
    vart_eredmeny = "gép veszett"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_vesztett_kevesebblap teszt sikeres")
    else:
        print("a gep_vesztett teszt_kevesebblap megbukott")


def gep_vesztett_tobblap():
    jatekos = [10, 10]
    gep = [10, 8, 3]
    vart_eredmeny = "gép veszett"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_vesztett_tobblap teszt sikeres")
    else:
        print("a gep_vesztett_tobbllap teszt megbukott")



def dontetlen_jatekos():
    jatekos =[10, 10]
    gep = [10, 6, 4]
    vart_eredmeny = "döntetlen,a játékos nyert"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a dontetlen teszt sikeres")
    else:
        print("a dontetlen teszt megbukott")


def dontetlen_gep():
    jatekos =[10, 3, 7]
    gep = [10, 10]
    vart_eredmeny = "döntetlen,a gép nyert"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a dontetlen teszt sikeres")
    else:
        print("a dontetlen teszt megbukott")

teszt_esetek()