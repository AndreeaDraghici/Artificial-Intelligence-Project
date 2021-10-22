import random


def generare_dimensiune_parcare():
    """Generam random dimensiunea parcarii m x m."""
    return random.randint(1, 7)


def generare_stare_initiala(dimensiune):
    """
       Generam starea initiala cu pozitia de pornire pentru fiecare vehicul, care reprezinta prima coloana a unei matrice,
       dar fiecare pozitie i, j din matrice este notata cu valori incepand de la 0 pana la dimensiunea parcarii astfel,
       daca i = 1 si j = 1 => pozitia va fi 0
       pentru i = 1 și j = 2 => pozitia va fi 1 si asa mai departe pana la ultima pozitie,
       care va fi egala cu numarul variabilei parking_size.
    """
    stare_initiala = tuple()  # privim starea initiala ca fiind un tuplu
    idx = 0  # idx poate fi privit ca un indice al starii vehiculului i
    while idx < dimensiune:
        stare_initiala += tuple([dimensiune * idx])
        idx += 1
    return stare_initiala  # returnam starea initiala a problemei ca fiind un tuplu


def generare_stare_finala(dimensiune, stare_initiala):
    """
       Generam starea obiectivului, urmand aceeasi idee ca mai sus, dar folosind o o alta formula, deoarece fiecare vehicul trebuie sa ajunga la
       pozitia cu coordonatele m - i + 1, m, asta inseamna ca trebuie sa ajunga pe randul de sus, dar în ordine inversa
    """
    stare_finala = tuple()  # privim starea finala ca fiind un tuplu
    idx = 0  # idx poate fi privit ca un indice al starii vehiculului i
    while idx < dimensiune:
        stare_finala += tuple([(dimensiune ** 2) - stare_initiala[idx] - 1])
        idx += 1
    return stare_finala  # returnam starea finala a problemei ca fiind un tuplu
