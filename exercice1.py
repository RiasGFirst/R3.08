
def plusGrand(a : int, b : int) -> int:
    """
    Retourne le nombre le plus grand des 2.
    :param a:
    :param b:
    """
    if a > b:
        return a
    else:
        return b


def superieur(a: int, seuil:int=10) -> str:
    """
    Retourne si le nombre est supérieur au seuil.
    :param a:
    :param seuil:
    """
    if a > seuil:
        return f"{a} est supérieur a {seuil}"
    else:
        return f"{a} est inferieur a {seuil}"


def superieurList(l:list) -> int:
    """
    verify each number and find the bigger
    :param l:
    :return:
    """
    n = 0
    for i in l:
        if i > n:
            n=i
    return n


def seuilList(l:list, seuil:int=3) -> list:
    """
    verify each number and find the bigger than the seuil then append it to the list
    :param l:
    :param seuil:
    :return:
    """
    n = []
    for i in l:
        if i < seuil:
            n.append(i)
    return n


def dicoAffiche(dico:dict, chain:str) -> str:
    """
    Print the value of each key in the dico preceded by the chain
    :param dico:
    :param chain:
    """
    for k, v in dico.items():
        print(f"{chain} {k} : {v}")


print(plusGrand(10, 5))
print(superieur(2))
print(superieurList([1, 2, 4, 3, 9]))
print(seuilList([1, 2, 4, 3, 9]))
dicoAffiche({"a": 1, "b": 2, "c": 10}, "valeur de")
