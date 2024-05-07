import math

def prixChemin(chemin: dict, nom):
    prixTotal = 0
    for destination, villes in chemin[nom].items():
        nom += " - " + destination
        prixTotal += villes
    return nom



villes = {
    "Brest": {"Paris": 53, "Lille": 151, "Marseille": 278},
    "Paris": {"Brest": 122, "Lille": 53, "Marseille": 186}
}
print(prixChemin(villes, "Brest"))

def decompDevises(prix : int) -> dict:
    if prix < 0:
        raise ValueError("Le prix est négatif")
    devisesPossibles = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    devises = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    for i in range(len(devisesPossibles) - 1, -1, -1):
        while prix >= devisesPossibles[i]:
            devises[devisesPossibles[i]] += 1
            prix -= devisesPossibles[i]
    return devises

def strDevises(prix : int) -> str:
    dictionnaire = decompDevises(prix)
    result = ""
    for key, value in dictionnaire.items():
        result += str(key) + " :" + str(value) + "€, "

    return result

print(strDevises(47))

def dicoVilles(tab : list) -> dict:
    tab.sort()
    dico = {}
    for i in range(len(tab)):
        dico[tab[i]] = i
    return dico


villes = ["Brest", "Strasbourg", "Marseille"]
print(dicoVilles(villes))

def verifVilles( n : int, dico : dict ) -> bool:
    for value in dico.values():
        if type(value) != int:
            raise TypeError("Ce n'est pas le bon type ")
        if not (0 <= n <= len(dico) - 1):
            raise ValueError("L'indice ne correspond pas")
    return True

def strCycle(tab : list) -> str:
    global villes
    result = ""
    for i in tab:
        result += villes[i] + " - "
    return result

print(strCycle([0,2,1,0]))

PRIX = [[0, 183.47, 156.77], [183.47, 0, 121.74], [156.77,
121.74, 0]]

def arrondiSup(tab2tabPrix : list) -> None:
    for i in range(len(tab2tabPrix)):
        for j in range(len(tab2tabPrix[i])):
            tab2tabPrix[i][j] = math.ceil(tab2tabPrix[i][j])
    
arrondiSup(PRIX)
print(PRIX)
      
def verifTab2prix(tab2tab : list) -> bool:
    for i in range(len(tab2tab)):
        for j in range(len(tab2tab[i])):
            if type(tab2tab[i][j]) != int:
                raise TypeError("Ce n'est pas le bon type ")
    return True

def nextVille(ville: int, villesDejaVisitees: list, tabPrix: list) -> tuple:
    if len(tabPrix) == 0:
        return (ville, math.inf)
    prix = min(tabPrix)
    tabPrix.pop(tabPrix.index(prix))
    print(prix)
    result = nextVille(ville + 1, villesDejaVisitees + [ville + 1], tabPrix)
    if result[1] < prix:
        return result
    return (ville, prix)

print("aaaaaaaaaa")
print(nextVille(0, [0], [0, 184,157]))

def cycleGloutonDepuisVille(villeD: int, tab2tabPrix: list) -> tuple:
    pass
