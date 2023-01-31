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
    teszt_esetek()
def jatekos_vesztett():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "jatekos veszett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")