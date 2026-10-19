print("Entrez votre âge :")
age = int(input())
if age <= 12:
    print("Billet : 25 dh")
else:
    etu = input("Êtes-vous étudiant ? Entrez O ou N : ")
    if etu == "O":
        print("Étudiant : 35 dh")
    else:
        print("Tarif normal : 50 dh")
#######################################33
import random
# # # 1. Tirer un nombre aléatoire entre 1 et 10
nombre_secret = random.randint(1, 10)
# # 2. Boucle pour demander à l'utilisateur de deviner
while True:
    devinette = int(input("Devine le nombre (entre 1 et 10) : "))
   # # 3. Vérifier si l'utilisateur a gagné
    if devinette == nombre_secret:
        print("Bravo, tu as gagné ! 🎉")
        break
    else:
        print("Ce n’est pas le bon nombre, essaye encore.")
########################################33
# # CREER FICHIER 
with open("bonjour.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Bonjour\nJe découvre la gestion des fichiers en Python")
#######################################33
# # MODIFIER UN MOT DANS UN TEXTE
import re 
 
texte = "Python est difficile" 
nouveau = re.sub("difficile", "facile", texte) 
print(nouveau) 
#######################################33
# #extraire les adresses e-mail valides 

import re 
 
emails = "Email : ali@gmail.com @gmail .com taha@yahoo.fr t@   " 
resultats = re.findall(r"\w+@\w+\.\w+", emails) 
print(resultats) 
#######################################33
# #lit le contenu d’un fichier texte
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        print("📄 Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    print("❌ Erreur : Le fichier 'data.txt' est introuvable.")
except Exception as e:
    print(f"⚠️ Une erreur est survenue : {e}")
#########################################33
#Questian:
# # quelle fonction donne le longueur d'une liste
# #  A)lenght() B)len() C)size()
# #   reponse : A ou B ou C
# # CORRECT OU INCORRECT
#Repnse
# # 📚 Question à choix multiple
print("Quelle fonction donne la longueur d'une liste ?")
print("  A) lenght()")
print("  B) len()")
print("  C) size()")

# 📝 Saisie de la réponse
reponse = input("Réponse (A, B ou C) : ").strip().upper()

# ✅ Vérification
if reponse == "B":
    print("✅ CORRECT : La fonction len() donne la longueur d'une liste.")
else:
    print("❌ INCORRECT : La bonne réponse est B) len().")
#######################33

# # Liste des questions sous forme de dictionnaires
questions = [
    {
        "question": "Quelle fonction donne la longueur d'une liste ?",
        "options": "A) lenght()\nB) len()\nC) size()",
        "reponse": "B"
    },
    {
        "question": "Quelle méthode met une chaîne en majuscules ?",
        "options": "a) upper()\nb) capitalize()\nc) big()",
        "reponse": "A"
    }
]

# Boucle sur chaque question
for q in questions:
    print("\n📚", q["question"])
    print(q["options"])
    
    # Saisie et normalisation de la réponse
    reponse = input("Ta réponse : ").strip().upper()
    
    # Vérification
    if reponse == q["reponse"].upper():
        print("✅ CORRECT !")
    else:
        print(f"❌ INCORRECT. La bonne réponse était {q['reponse'].upper()}")
########################

A= 2
B = 3
print("la somme de A+B= " , A+B)
print("la deffernce de A-B=", A-B)

########################
import numpy as np

A = np.array([[1, -2], [3, 0]])
k = 3

produit = k * A
print("k × A =\n", produit)