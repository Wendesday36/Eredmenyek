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

teszt_esetek()