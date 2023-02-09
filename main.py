# megoldas
def eredmeny(jatekoskatya: [int], gepkartya: [int]):
    jatekosp: int = osszeg(jatekoskatya)
    gepp: int = osszeg(gepkartya)
    jatekdb: int = len(jatekoskatya)
    gepdb: int = len(gepkartya)
    e: str = ""
    if jatekosp <= 21 and gepp <= 21:
        if jatekosp > gepp:
            e = "játékos nyert"
        elif gepp > jatekosp:
            e = "gép nyert"
        elif gepp == jatekosp:
            if jatekdb > gepdb:
                e = "gép vesztett"
            elif gepdb > jatekdb:
                e = "játékos vesztett"
            else:
                e = "döntetlen,osztoztok a nyereményen"
    else:
        if jatekosp > 21:
            e = "játékos vesztett"
        if gepp > 21:
            e = "gép vesztett"
        if jatekosp > 21 and gepp > 21:
            e = "döntetlen, a ház nyert"
    return e



def osszeg(kartyak: [int]):
    pontok: int = 0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok


#teszt esetek


def teszt_esetek():

    jatekos_vesztett()
    jatekos_vesztett_kevesebb()
    jatekos_vesztett_tobb()
    gep_vesztett()
    gep_vesztett_tobblap()
    gep_vesztett_kevesebblap()
    dontetlen()
    dontetlen_gep()
    dontetlen_jatekos()
    jatekos_nyer21()
    jatekos_nyer19()
    jatekos_nyer18()
    gep_nyert()
    gep_nyert19()
    gep_nyert19kev()
def jatekos_vesztett():
    jatekoskartya = [10, 8]
    gepkartya = [10, 10]
    vart_eredmeny = "gép nyert"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def jatekos_vesztett_kevesebb():
    jatekoskartya = [10, 9]
    gepkartya = [10, 10, 1]
    vart_eredmeny = "gép nyert"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett_kevesebb teszt sikeres")
    else:
        print("a jatekos_vesztett_kevesebb teszt megbukott")


def jatekos_vesztett_tobb():
    jatekoskartya = [10, 10, 1]
    gepkartya = [10, 10]
    vart_eredmeny = "gép nyert"
    kapott_eredmeny = eredmeny(gepkartya, jatekoskartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett_tobb teszt sikeres")
    else:
        print("a jatekos_vesztett_tobb teszt megbukott")


def gep_vesztett():
    jatekoskartya = [10, 10, 2]
    gepkartya = [10, 10]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(gepkartya, jatekoskartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_vesztett teszt sikeres")
    else:
        print("a gep_vesztett teszt megbukott")


def gep_vesztett_kevesebblap():
    jatekoskartya = [10, 10]
    gepkartya = [10, 8, 4]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_vesztett_kevesebblap teszt sikeres")
    else:
        print("a gep_vesztett teszt_kevesebblap megbukott")


def gep_vesztett_tobblap():
    jatekoskartya = [10, 10]
    gepkartya = [10, 8, 3]
    vart_eredmeny = "játékos nyert"
    kapott_eredmeny = eredmeny(gepkartya, jatekoskartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_vesztett_tobblap teszt sikeres")
    else:
        print("a gep_vesztett_tobblap teszt megbukott")


def dontetlen():
    jatekoskartya = [10, 6]
    gepkartya = [10,6]
    vart_eredmeny = "döntetlen,osztoztok a nyereményen"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a dontetlen teszt sikeres")
    else:
        print("a dontetlen teszt megbukott")


def dontetlen_jatekos():
    jatekoskartya =[10, 10]
    gepkartya = [10, 6, 4]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(gepkartya, jatekoskartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a dontetlen_jatekos teszt sikeres")
    else:
        print("a dontetlen_jatekos teszt megbukott")


def dontetlen_gep():
    jatekoskartya =[10, 3, 7]
    gepkartya = [10, 10]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gepkartya, jatekoskartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a dontetlen_gep teszt sikeres")
    else:
        print("a dontetlen_gep teszt megbukott")





def jatekos_nyer21():
    jatekoskartya =[10, 4, 7]
    gepkartya = [10, 10, 4]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_nyer21 teszt sikeres")
    else:
        print("a jatekos_nyer21 teszt megbukott")





def jatekos_nyer19():
    jatekoskartya = [10, 7, 2]
    gepkartya = [10, 5]
    vart_eredmeny = "játékos nyert"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_nyer19 teszt sikeres")
    else:
        print("a jatekos_nyer19 teszt megbukott")






def jatekos_nyer18():
    jatekoskartya =[10, 9]
    gepkartya = [10, 7, 5]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_nyer18 teszt sikeres")
    else:
        print("a jatekos_nyer18 teszt megbukott")





def gep_nyert():
    jatekoskartya =[10, 10]
    gepkartya = [10, 7, 4]
    vart_eredmeny = "gép nyert"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_nyert teszt sikeres")
    else:
        print("a gep_nyert teszt megbukott")









def gep_nyert19():
    jatekoskartya =[10, 8]
    gepkartya = [10, 7, 2]
    vart_eredmeny = "gép nyert"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_nyert19 teszt sikeres")
    else:
        print("a gep_nyert19 teszt megbukott")


def gep_nyert19kev():
    jatekoskartya = [10, 8, 4]
    gepkartya = [10, 9]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(jatekoskartya, gepkartya)
    if kapott_eredmeny == vart_eredmeny:
        print("a gep_nyert19kev teszt sikeres")
    else:
        print("a gep_nyert19kev teszt megbukott")


teszt_esetek()