from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import csv  

def string_liste(string: str): #convertit string en lite
    resultat = []
    for u in string:
        resultat.append(u)
    return resultat
    
def liste_string(liste: list): #convertit liste en string 
    resultat = ""
    for t in liste:
        resultat += str(t)
    return resultat

class graphe:
    def __init__(self, titre = "", labelx = "", labely = ""):
        plt.title(titre)
        plt.ylabel(labely)
        plt.xlabel(labelx)

    class points():
        def __init__(self, liste_points = []):
            self.x = []
            self.y = []
            for i in liste_points:
                self.x.append(i[0])
                self.y.append(i[1])

        def exporter(self,nom = "grappyExport"):
            with open(nom+".csv", "w") as export:
                graveur = csv.writer(export)  #pb acces aux labels
                graveur.writerow(["labelx","labely"])
                for i in range (len(self.x)):
                    graveur.writerow([self.x[i], self.y[i]])
      
        def afficher(self):
            plt.plot(self.x, self.y)
            plt.show()

    class importer:
        def __init__(self, nom_fichier: str, configuarion: str, logiciel="excel"): #configuration = horizontale (h) ou verticale (v), logiciel (excel vs numbers)
            deli = ""
            if logiciel == "numbers":  #excel et numbers n'utilisent pas le meme delimiteur 
                deli = ";"
            elif logiciel == "excel":
                deli = ","
            else:
                raise ValueError("Erreur, il n'y a pas de delimiteur connu pour " + logiciel + " ,veuillez essayer avec excel ou numbers.")
            with open(nom_fichier, "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=deli)

                if configuarion not in ["v", "h"]:
                    raise ValueError("Erreur: " + configuarion + " n'est pas une configuration valide, seul v (verticale) et h (horizontale) sont possibles.")

                self.x = []
                self.y = []

                if configuarion == "v":
                    for label in csv_reader:
                        plt.xlabel(label[0])
                        plt.ylabel(label[1])
                        break

                    for ligne in csv_reader:
                        self.x.append(ligne[0])
                        self.y.append(ligne[1])
                else:
                    for ligne in csv_reader:
                        for x in range(len(ligne)):
                            self.x.append(ligne[x])
                        for y in range(len(ligne)):
                            self.y.append(ligne[y])
                        break
                    plt.xlabel(self.x.pop(0))
                    plt.ylabel(self.y.pop(0))


        def afficher(self):
            plt.plot(self.x, self.y)
            plt.show()

    class fonction:
        def __init__(self, fonction: str, xdebut: float, xfin: float, pas: float = 1): #le pas est optionnel est de base sera egal à 1
            self.x = []
            self.y = []
            self.fonction = fonction
            copieFonction = string_liste(fonction)
            for i in range ((xfin-xdebut) + 1):                                         #pb de priorite, il faut rajouter des parenthese autour du x pour le cas ou x est negatif
                while "x" in copieFonction:                                             # donc je rajoute des parenthese autour de chaque x
                    indice = copieFonction.index("x")
                    copieFonction[indice] = xdebut
                    copieFonction.insert(indice, "(")
                    copieFonction.insert(indice+2, ")")
                self.x.append(xdebut)
                xdebut = xdebut + pas
                self.y.append(eval(liste_string(copieFonction)))
                copieFonction = string_liste(fonction)
                
        def afficher(self):
            plt.plot(self.x, self.y)
            plt.show()