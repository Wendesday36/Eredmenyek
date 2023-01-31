#megoldas
def eredmeny(jatekoskatya: [int], gepkartya : [int]):
    if osszeg(jatekoskatya) > 21 :
        print("vesztett")
    if osszeg(gepkartya) > 21:
        print("vesztett")

    #tesztesetek

def osszeg(kartyak: [int]):
    pontok: int=0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok