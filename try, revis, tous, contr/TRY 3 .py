note1 = float(input("Note 1 : "))
note2 = float(input("Note 2 : "))
note3 = float(input("Note 3 : "))
moyenne = (note1 + note2 + note3) / 3
# print("Moyenne :", moyenne)
if moyenne > 20 :
    print("errur : le note doit etre inferieur strictement 21.")
elif moyenne < 0 :
    print("errur : la note doit etre psitif.")
else:
    print(f"la moyenne est : {moyenne}/20.")
    print("trés bien continue")
########################
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur * self.largeur
r = Rectangle(5, 3)
print("Surface :", r.surface())
#######################
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retier(self, montant):
        self.solde -=montant

    def afficher(self):
        print(f"{self.titulaire} : {self.solde} DH")

c = CompteBancaire("Mohamed", 1000)
c.deposer(500)
c.retier(100)
# c.afficher()
c.deposer(500)
c.retier(100)
c.retier(100)
c.afficher()
#######################
import time

print(" Exercice : Trouve le mot le plus long dans ta phrase.")
print(" Exemple : 'Python est un langage puissant et accessible'")

#  Démarrer le chronomètre
debut = time.time()

#  Entrée utilisateur
phrase = input(" Entre ta phrase : ")   
#    #la pomme de Amellagou est la plus cher et la plus consommés au marché marocan

#  Arrêter le chronomètre
fin = time.time()
duree = fin - debut

#  Traitement
mots = phrase.split()
mot_plus_long = max(mots, key=len)

#  Résultat
print(f" Le mot le plus long est : '{mot_plus_long}'")
print(f" Temps de réponse : {duree:.2f} secondes")
#########################33

from collections import namedtuple 
SuperHero = namedtuple('SuperHero',['nom', 'pouvoir', 'niveau'])
hero1 = SuperHero(nom="Iron Man", pouvoir="Armure technologique", niveau=85)
hero2 = SuperHero(nom="Thor", pouvoir="Marteau magique", niveau=95)
hero3 = SuperHero(nom="Spider-Man", pouvoir="Agilité et toile", niveau=80)
for hero in [hero1, hero2, hero3]:
    print(f"Nom: {hero.nom}, Pouvoir: {hero.pouvoir}, Niveau: {hero.niveau}")
def comparer_heros(hero1, hero2):
    if hero1.niveau > hero2.niveau:
        return f"{hero1.nom} est plus puissant que {hero2.nom}"
    elif hero1.niveau < hero2.niveau:
        return f"{hero2.nom} est plus puissant que {hero1.nom}"
    else:
        return f"{hero1.nom} et {hero2.nom} sont aussi puissants"
print(comparer_heros(hero1, hero2, ))






