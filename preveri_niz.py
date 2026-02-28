# This was the first file I made before making any of the other ones,
# for obvious reasons it's useless; no point in using arrays/lists
# when it's obviously better to use sets cause of O(1) lookup time.



testna_databaza = ['GCD and LCM', 'Mate in One', 'Major or Minor']

def poisci_element(tab, elt):
    """Preveri ali dan element obstaja v neurejeni tabeli
        in vrne True ce obstaja, False sicer"""
    from random import randint  
    # bomo uporabili nakljucne stevilke za izbir pote, kar je 
    # boljs kot ce vsakic gremo levo ali vsakic desno (manjsa verjetnost da dobimo worst case (mislim))
    
    smer = randint(0, 1)

    if smer == 0:
        for i in range(len(tab)):
            if tab[i] == elt:
                return True
    else:  # ce je smer desno, oz. 1
        for i in range(len(tab) - 1, -1, -1):
            if tab[i] == elt:
                return True
    return False



def poisci_urejen_element(tab, elt):
    """Preveri ali dan element obstaja v urejeni tabeli
      s bisekcijo in vrne True ce obstaja, False sicer"""
    while len(tab) > 0:
        sredina = len(tab) // 2

        if tab[sredina] == elt:
            return True
        elif len(tab) == 1:
            break
        elif tab[sredina] > elt:
            tab = tab[:sredina]
        else:  # ce je element levo
            tab = tab[sredina:]
    return False



def preveri_niz(niz):
    """Preveri, ali dan niz obstaja v kaksni databazi,
        ce je dovolj podoben, potem da ustrezen kot predlog"""
    niz = niz.split()
    nov_niz = []
    for beseda in niz:
        nov_niz.append(beseda.lower())

    if poisci_element(testna_databaza, niz):
        pass

    return nov_niz


print(poisci_element(testna_databaza, "GCD and LCM"))
print(poisci_element([1,2],1))
print('////////')

print(poisci_urejen_element([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31], 1))
print(poisci_urejen_element([], 5))
print(poisci_urejen_element(['a', 'b', 'c', 'd', 'e'], 'd'))

print(preveri_niz('GCD and LCD'))



# prvin proveri dali voopsto postoi vnesenata niza
# proveri dali postoi vnesata vo drugata databaza odnosno dali e veke rezervirana
