"""
On cherche les nombres premiers 
"""
from math import sqrt


#### Fonction secondaire


def isprime(p):
    """
    Retourne un booléen indiquant si le nombre est premier ou non
    """
    nb = p
    premier = True
    if nb == 0 :
        return False
    if nb == 1 :
        return False
    for i in range(int(sqrt(nb))+1):
        if i == 0:
            continue
        if i == 1:
            continue
        if i == p:
            continue
        if nb % i == 0:
            premier = False
    return premier

#### Fonction principale


def main():
    """
    Retourne la liste des nombres premiers 
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
