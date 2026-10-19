# #1 — Syntaxe de base, commentaires, indentation
# #Règles simples 
# # Ceci est un commentaire 
# print("Bonjour le monde")  # affiche du texte 
# """ Ceci est un docstring ou commentaire 
# sur plusieurs lignes (utilisé aussi pour documenter). """
# #2 — Variables & types (int, float, str, bool, None)
# # On assigne avec = : nom = valeur  
# a = 10          # int 
# b = 3.14        # float 
# nom = "Abderrahman"   # str (chaîne) 
# est_vrai = True # bool 
# rien = None     # NoneType (absence de valeur) 
# #Vérifier le type : type(variable) 
# print(type(a))      # <class 'int'> 
# print(type(b))      # <class 'float'>
# #Constantes 
# # • Python n'a pas de constantes natives. Par convention on écrit les noms en MAJUSCULES : 
# PI = 3.14159 
# MAX_USERS = 100 
# #Règles de nommage 
# # • Commence par une lettre ou _, pas de chiffres au début. 
# # • Pas d'espaces, utilise _ pour séparer : ma_variable 
# # • Respecte les noms clairs.
# Exemple complet de conversion d'input :  
# age = int(input("Ton âge ? "))   # input() renvoie une str, on la convertit en int 
# taille = float(input("Ta taille en mètre ? ")) 
# print(f"Dans 5 ans, tu auras {age + 5} ans.") 

# # Exemples concrets — courts et parlants 
# # 1. Réaffectation (typage dynamique)  
# x = 5          # x est int 
# x = "cinq"     # maintenant x est str 
# # 2. Calcul simple 
# a = 7 
# b = 2 
# print(a + b)   # 9 
# print(a / b)   # 3.5 (division flottante) 
# print(a // b)  # 3   (division entière / floor) 
# print(a % b)   # 1   (reste) 
# print(a ** b)  # 49  (exponentiation) 
# print(a ** b)  # 49  (exponentiation) 
# # 3. Affichage élégant avec f-string (Python 3.6+) 
# nom = "Abderrahman" 
# age = 20 
# print(f"{nom} a {age} ans.")  # Abderrahman a 20 ans. 
##############################
# ##Exercice simple — périmètre et aire d'un rectangle 
# #Enoncé : lire longueur et largeur (réels), afficher périmètre et aire.  # Solution :  
# # Lecture (input renvoie une chaîne -> on convertit en float) 
# longueur = float(input("Longueur du rectangle (m) : ")) 
# largeur = float(input("Largeur du rectangle (m) : ")) 
# # Calculs 
# perimetre = 2 * (longueur + largeur) 
# aire = longueur * largeur 
# # Affichage 
# print(f"Le périmètre est {perimetre} m") 
# print(f"L'aire est {aire} m²") 
### une autre methode :
# # Enoncé : lire longueur et largeur (réels), afficher périmètre et aire. 
# longueur = float(input ("Entrez un nombre : "))
# largeur = float(input ("Largeur du rectangle (m) : "))
# périmètre = 2 * (longueur + largeur)
# aire =  largeur * longueur
# print(f" \nLe périmètre est {périmètre} m") 

# print (' \nle périmite de rectangle en (m) est : ' , {périmètre} ,'(m)')

# print (" \nl'aire de rectangle en m² est : " , aire, 'm²')
######################
# #Petits exercices 
# # 1. Écris un script qui demande un nombre et affiche son double. 
# # 2. Demande deux nombres et affiche leur moyenne. 
# # 3. Demande un nombre entier et affiche si c'est pair ou impair. (Indice : utilise % 2) 
## 1
# X = int (input (" Entrez un nombre : "))
# print(f" le double de X :", {X * 2})
# ## 2
# notes = [float(x) for x in input("Entrez les notes séparées par des espaces : ").split()]
# moyenne = sum(notes) / len(notes)
# print("La moyenne est :", moyenne)
# ##
# # Demander deux nombres séparés par un espace
# r = list(map(int, input("Entrez deux nombres séparés par l'espace : ").split()))
# # Calculer la moyenne
# moyenne = sum(r) / len(r)
# # Afficher le résultat
# print("La moyenne est :", moyenne)
# # ##
# # Demander 7 nombres à l'utilisateur
# nombres = [] # LA LISTE EST VIDE 0
# for i in range(7):
#     valeur = float(input(f"Entrez le nombre {i+1} :")) # Demande une saisie au clavier - Affiche un texte dynamique (ici le numéro du tour)
#     nombres.append(valeur) # 👉 Prends la valeur entrée par l’utilisateur et ajoute-la à la liste 
#                            # - ajoute la valeur saisie à la fin de la liste.
# moyenne = sum(nombres) / len(nombres)
# print("La moyenne des 7 nombres est :", moyenne)
# # ##
# numbr = []
# for i in range (3):
#     valu = float(input(f"Entrez le nombre {i + 1} : "))
#     numbr.append(valu)
# moyen = sum(numbr) / len(numbr)
# print ("La  moynnnnnnne de 3 nombre est : ",moyen)
## 3
# y = int(input("entrez un entier : "))
# if y % 2 == 0  :
#    print( f"{y} est un pair.")
# else :
#     print( f"{y} est impair.")
# #
# nombre = int(input("Entrez un nombre : "))
# if nombre % 2 == 0:
#     print("Le nombre est pair.")
# else:
#     print("Le nombre est impair.")
##################
#Exercices pour t’entraîner 
# Demander à l’utilisateur deux nombres et afficher : 
# • leur somme 
# • leur différence 
# • leur produit 
# • leur quotient 
# a = float(input("Entrez le premier nombre : "))
# b = float(input("Entrez le deuxième nombre : "))
# somme = a + b
# difference = a - b
# produit = a * b
# if b != 0:
#     quotient = a / b
# else:
#     quotient = "Impossible (division par zéro)"
# print("La somme est :", somme)
# print("La différence est :", difference)
# print("Le produit est :", produit)
# print("Le quotient est :", quotient)
####################
# # # P 7 :
# Lire le rayon d’un cercle et afficher son périmètre et son aire. 
# Formules : 
# • P = 2 × π × r 
# • A = π × r² 
# (tu peux utiliser PI = 3.1416) 

# r = int (input("Entrez le rayon de cercle : "))
# PI = 3.1416
# p = 2 * PI * r
# a = PI * (r**2) 
# print (f"le péremetre de cercle est",p)
# print (f"l'aire de cercle est",a)

##########Lire un nombre entier et afficher le reste de la division par 5. 
# y =float (input("Entrez un nombre :"))
# z = y % 5
# print ("le reste de la division par 5 :", z)
###########
# note = float(input("Note de l’examen : ")) 
# if note >= 16: 
#  bonus = 3 
# elif note >= 14: 
#  bonus = 2 
# elif note >= 10: 
#  bonus = 1 
# else: 
#  bonus = 0 
# print(f"Bonus obtenu : {bonus} points") 
############
# age = int(input("Entrez votre âge : ")) 
# if age >= 18 and age < 60: 
#   print("Adulte") 
# elif age >= 60: 
#  print("Senior") 
# else: 
#  print("Mineur") 

##############################
# Exercice 1 
# Y = int (input(" Entrez un nombre entier : "))
# if Y > 0 :
#     print ("Positif")
# elif Y < 0 :
#     print ("Négatif")
# else :
#     print ("Nul")
###########################
# Exercice 2
# A = int(input("Entrez un entier: "))
# B = int(input("Entrez un entier: "))
# if A > B :
#     print ('A est supériur à B')
# elif A < B :
#     print ('A est inférieur à B')
# else : 
    # print ('A est égale à B')

# # # une autre maniére 1 :
# # Entrer deux nombres séparés par un espace
# A, B = map(int, input("Entrez deux entiers séparés par un espace: ").split())
# # Comparaison
# if A > B:
#     print("A est supérieur à B")
# elif A < B:
#     print("A est inférieur à B")
# else:
#     print("A est égal à B")
# # Afficher le plus grand des deux
# maximum = max(A, B)
# print("Le plus grand des deux nombres est :", maximum)

# # # une autre maniére 2 OU bien exercice 3 :
# # Entrer trois nombres séparés par des espaces
# A, B, C = map(int, input("Entrez trois entiers séparés par des espaces : ").split())
# # Comparaison entre A et B
# if A > B:
#     print("A est supérieur à B")
# elif A < B:
#     print("A est inférieur à B")
# else:
#     print("A est égal à B")
# # Comparaison entre A et C
# if A > C:
#     print("A est supérieur à C")
# elif A < C:
#     print("A est inférieur à C")
# else:
#     print("A est égal à C")
# # Comparaison entre B et C
# if B > C:
#     print("B est supérieur à C")
# elif B < C:
#     print("B est inférieur à C")
# else:
#     print("B est égal à C")
# # Afficher le plus grand des trois
# maximum = max(A, B, C)
# print("Le plus grand des trois nombres est :", maximum)

# # # une autre maniére 3 :
# Entrer six nombres séparés par des espaces
# A, B, C, D, E, F = map(int, input("Entrez six entiers séparés par des espaces : ").split())
# # Afficher le plus grand des six
# maximum = max(A, B, C, D, E, F)
# print("Le plus grand des six nombres est :", maximum)
#################################
#Exercice 4 P 10
# annee = int(input("Entrez une année : ")) 
# if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0): 
#  print("Année bissextile") 
# else: 
#  print("Année non bissextile")
############################ 
# #Exercice 5 P 10
# # note = [15, 17, 16, 18, 20  ]
# note = [-10, 10, 13, 15, -12  ]
# print("note : ", note)
# moyenne = sum(note)/ len(note) 
# if moyenne >= 16:
#     print("Admis avec mention Très Bien")
# elif moyenne >= 14:
#     print("Admis avec mention Bien")
# elif moyenne >= 12 :
#     print("Admis avec mention Assez Bien")
# elif moyenne >= 10 :
#     print ("Admis")
# elif 0 < moyenne < 10 :
#     print("Refusé")
# else :
#     print("n'est pas execist, Ressseyer.")
############## P: 10
# for i in range (6):
#     print(i)
# # ##
#     # Example 1: space-separated
# print(" ".join(["apple", "banana", "cherry"]))
# # Output: apple banana cherry

#     # Example 2: comma-separated
# print(", ".join(["apple", "banana", "cherry"]))
# # Output: apple, banana, cherry

#     # Example 3: no separator
# print("".join(["a", "b", "c"]))
# # Output: abc
# # # #
# print("Bonjour Mohamed !")
# # # #
# for i in range(6):
#     print("Bonjour Mohamed,", i, end=" ")
# # # ##
# print(" ".join("Mohamed " + str(i) for i in range(6)))
############## Résumer : entre *join et *end=" "
# for i in range(6):
#     print(i, end=" ")

# print(" ".join(str(i) for i in range(6)))
####################
# for lettre in "Pythoooooooon": 
#  print(lettre,end=" ") #pour afficher un nom lettre par lettre 
# ############################
# somme = 0
# for i in range (0, 10):
# #   print ("la somme des premiére nombre de 0 à 10 est :", {i})
#     somme += i
#     print(somme, end=  " ")
# # #
# somme = 0
# for i in range(1, 11):   # من 1 إلى 10
#     somme += i
# print("Bonjour Mohamed, la somme est:", somme)
################### while
# i = 1 
# # i  += 1
# while i <= 5: 
#     i  += 1
#     print(i)
#     i  += 1
#################
# somme = 0 
# n = int(input("Entrez un nombre (0 pour arrêter) : ")) 
 
# while n != 0: 
#     somme += n 
#     n = int(input("Entrez un nombre (0 pour arrêter) : ")) 
 
# print(f"Somme totale : {somme}") 
#######################
# #break # - break: يوقف الحلقة نهائياً
# for i in range(1, 10): 
#     if i == 5: 
#         break 
#     print(i) 
# # affiche 1 2 3 4 
############## #continue - continue sert à sauter une itération sans exécuter le reste du bloc.
                         #- Ici, il permet d’ignorer l’affichage du nombre 3
                         #- continue: يتجاهل الدورة الحالية فقط ويكمل باقي الحلقات.
# for i in range(1, 6): 
#     if i == 3: 
#         continue 
#     print(i) 
# affiche 1 2 4 5 
################# P :13
#Exemple : afficher les nombres pairs de 1 à 10 
# for i in range(1, 11): 
#   if i % 2 == 0: 
#    print(i) 
###############33
# #Exemple : calculer la factorielle d’un nombre 
# n = int(input("Entrez un entier : ")) 
# fact = 1 
# for i in range(1, n + 1): 
#    fact *= i 
# print(f"Factorielle de {n} = {fact}")
# ############
# for i in range(1, 4):         # lignes 
#     for j in range(1, 4):     # colonnes 
#       print(i * j, end="\t") 
#     print()  # saut de ligne 
# ################ P: 13
# # EXE 1 : Afficher les nombres de 1 à 10. 
# for i in range (1, 11):
#    print (i, end=", ")
# EXE 2 : Afficher les 10 premiers nombres pairs. 
# i = 0
# for i in range (0, 100):
#     if i % 2 == 0:
#      if i <= 20 :
#       print(i)
# EXE 3 : Afficher la somme des entiers de 1 à N (N lu au clavier). 
# Lire N au clavier
# N = int(input("Entrez un entier N : "))
# # Calcul avec la formule
# somme = N * (N + 1) // 2
# print("La somme des entiers de 1 à", N, "est :", somme)
# + EXE 3 : Afficher la somme des entiers de 1 à N (N lu au clavier). 
# somme = 0
# for i in range (1, 100):
#    somme = i + somme
# print (somme)
# EXE : 4  P= 14 : Afficher la table de multiplication d’un nombre donné (ex : table du 7). 
# n =  7  # int(input ("Entrez un nombre : "))
# for i in range (0 , 13):
#    multi = n * i
#    print(multi)
# Exercice 5 : Lire 10 nombres et afficher la somme, le maximum et la moyenne
# nombres = []
# for i in range(10):
#     nb = float(input(f"Entrez le nombre {i+1} : "))
#     nombres.append(nb)
# somme = sum(nombres)
# maximum = max(nombres)
# moyenne = somme / len(nombres)
# print("Somme des nombres :", somme)
# print("Maximum des nombres :", maximum)
# print("Moyenne des nombres :", moyenne)

# # #  Exercice 5 : Lire 10 nombres et afficher la somme, le maximum et la moyenne
# somme = 0
# maximum = None   # au départ, pas de maximum défini
# for i in range(10):
#     nb = float(input(f"Entrez le nombre {i+1} : "))
#     somme += nb
#     if maximum is None or nb > maximum:
#         maximum = nb
# moyenne = somme / 10
# print("Somme des nombres :", somme)
# print("Maximum des nombres :", maximum)
# print("Moyenne des nombres :", moyenne)
#################3 En pseudo-code simple (sans liste) 
#### Somme ← 0
#### Maximum ← non défini
#### Pour i de 1 à 10 :
####     Lire nombre
####     Somme ← Somme + nombre
####     Si Maximum est non défini OU nombre > Maximum :
####         Maximum ← nombre
#### Moyenne ← Somme / 10
#### Afficher Somme, Maximum, Moyenne
###################35
# EXE : 6 Afficher un triangle d’étoiles : P=14
# for i in range (1, 6): # de 1 à 5
#     print("*"*i)
###############333
##LES FONCTIONS en Python
# #Une fonction est un bloc de code qui exécute une tâche spécifique, et que tu peux appeler à tout moment 
   # dans ton programme. 
# # ~#Exemple simple :  
# def saluer(): 
#   print("Bonjour !") 
# saluer()  # appel de la fonction 
# ## exple chez moi
# def allah_okbar() :
#   print('alhamdu lilah Ala niAmatih .')
# allah_okbar()
# # Structure d’une fonction 
# def nom_de_fonction(paramètres): 
#    # bloc d’instructions 
#     return valeur
################ 
# def somme(a, b, c): 
#   resultat = a + b + c
#   return resultat 
# # Appel 
# x = somme(5, 3, 2) 
# print(f"La somme est {x}") 
############
# def moyenne(a, b, c): 
#    return (a + b + c) / 3 
# m = moyenne(12, 15, 10) 
# print(f"Moyenne = {m}") 
############## Les variables locales et globales 
# • Une variable locale existe seulement à l’intérieur d’une fonction. 
#• Une variable globale est définie en dehors et accessible partout. 
#Exemple :  
# x = 10  # variable globale 
# def afficher(): 
#    y = 5  # variable locale 
#    print(x + y) 
# afficher()  # fonctionne 
# # print(y)  --> erreur (y n’existe pas ici) 
###################""
# def perimetre(longueur, largeur): 
#     return 2 * (longueur + largeur) 
# def aire(longueur, largeur): 
#     return longueur * largeur 
# # Programme principal 
# L = float(input("Longueur : ")) 
# l = float(input("Largeur : ")) 
# print(f"Périmètre = {perimetre(L, l)}") 
# print(f"Aire = {aire(L, l)}") 
##############3
# def carre(x): 
#        return x * x 
# def somme_carres(a, b): 
#         return carre(a) * carre(b)  
# print(somme_carres(2, 3))  # 13 
# ############3
# def saluer(nom="ami"): 
#     print(f"Bonjour {nom} !") 
# saluer()           # Bonjour ami ! 
# saluer("Abderrahman")   # Bonjour Abderrahman ! 
# saluer("BEN ALI Mohamed")
#####################
# nombres = [1, 5, 2, 8, 3, 10, 7]
# # etape 0 : ordre les nombres
# ordre = sorted(nombres, reverse=True)
# print(ordre)
# # Résultat : [10, 8, 7, 5, 3, 2, 1]
# # Étape 1 : doubler chaque nombre
# nombres_doubles = map(lambda x: x * 2, nombres)
# # Résultat : [2, 10, 4, 16, 6, 20, 14]
# # Étape 2 : garder les pairs
# pairs = filter(lambda x: x % 2 == 0, nombres_doubles)
# # Résultat : [2, 10, 4, 16, 6, 20, 14] (tous sont pairs)
# # Étape 3 : trier décroissant
# resultat = sorted(pairs, reverse=True)
# print(resultat)
# # Résultat final : [20, 16, 14, 10, 6, 4, 2]
# ################  ⚡ Variante plus lisible avec list comprehension
# nombres = [1, 5, 2, 8, 3, 10, 7]
# resultat = sorted([x*2 for x in nombres if (x*2) % 2 == 0], reverse=True)
# print(resultat)
# ############## 🧪 Si tu veux filtrer les pairs avant de les doubler 
# nombres = [1, 5, 2, 8, 3, 10, 7]
# pairs_originaux = filter(lambda x: x % 2 == 0, nombres)
# nombres_doubles = map(lambda x: x * 2, pairs_originaux)
# resultat = sorted(nombres_doubles, reverse=True)
# print(resultat)  # [20, 16, 4]
###################### 1.Filtrer les nombres pairs 
#                # - Avec lambda :
# nombres = [1, 2, 3, 4, 5, 6]
# pairs = list(filter(lambda x: x % 2 == 0, nombres))
# print(pairs)  # [2, 4, 6]
# # # - Avec def :
# nombres = [1, 2, 3, 4, 5, 6]
# def est_pair(x):
#     return x % 2 == 0
# pairs = list(filter(est_pair, nombres))
# print(pairs)  # [2, 4, 6]
# ############# 2. Doubler chaque nombre
#               #- Avec lambda :
# nombres = [1, 2, 3, 4, 5, 6]
# doubles = list(map(lambda x: x*2, nombres))
# print(doubles)  # [2, 4, 6, 8, 10, 12]
# # # # - Avec def :
# nombres = [1, 2, 3, 4, 5, 6]
# def doubler(x):
#     return x*2
# doubles = list(map(doubler, nombres))
# print(doubles)  # [2, 4, 6, 8, 10, 12]
#            # Exercices d’application 
# EXE 1 : Écrire une fonction carre(x) qui renvoie le carré d’un nombre.
# y= float(input("Entrez un reel : "))
# def carre(y):
#     return y**2
# print (carre(3)) # IF YOU NOT TO INPUT A NUMBRE 
# d = carre(y)
# print(d)
# # # +
# valeurs = input("Entrez des réels séparés par des espaces : ").split()
# def carre(x):
#     return x**2
# # Appliquer la fonction à chaque valeur
# resultats = [carre(float(v)) for v in valeurs]
# print(resultats)
############# EXE 2
# # Écrire une fonction maximum(a, b) qui renvoie le plus grand des deux nombres. 
# a = int (input("Entrez un entier A:"))
# b = int (input("Entrez un entier B:"))
# def maximum (a, b):
#     return max(a, b)
# maxx = maximum(a, b)
# print(f"le nombre le plus max entre {a} et {b} est : {maxx}")
# # +
# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# # Exemple d'utilisation
# x = float(input("Entrez le premier nombre : "))
# y = float(input("Entrez le deuxième nombre : "))
# print("Le plus grand est :", maximum(x, y))
############# EXE 3
# #Écrire une fonction est_pair(n) qui renvoie True si n est pair, sinon False. 
# def est_pair(n):
#     if n % 2 == 0 :
#         return True
#         # print (f"{n} est pair.")             
#     else :
#         return False
#         # print ( f"{n} est impair.")
#  #print(est_pair(5)) # there you choose the numbre
# y = float ( input ("Entrez l'entier :"))
# print(est_pair(y))
############ EXE 4 :
# #Écrire une fonction conversion(celsius) qui convertit une température en Fahrenheit. 
   #  #Formule : F = C × 9/5 + 32 
# def conversion(C):
#     F = (C * 9/5) + 32 
#     return F
# # print(conversion(25))   # 77.0
# C = int (input ("lhma: ")) 
# print(conversion(C))
############ EXE 5 :
#Créer un programme principal qui : 
    #1. Demande deux nombres à l’utilisateur 
    #2. Calcule la somme, la différence, le produit et le quotient en appelant des fonctions. 
# A = int (input("Entrez le premiere nombre :"))
# B = int (input("Entrez le deuxieme nombre :"))
# def somme(A, B):
#     sommee = A + B
#     return sommee
# # # OR return A + B
# def différence(A, B):
#     différence = A - B 
#     return différence
# # # OR return A - B
# def produit (A, B):
#     produit = A * B
#     return produit
# # # OR return A * B
# def quotient (A, B):
#     if B != 0 :
#        return A / B
#     else :
#         return "Erreur : division par zéro"
# def main():   #  main() regroupe toutes les opérations que le programme doit exécuter
#  print(somme(A, B))      
#  print(différence(A, B)) 
#  print(produit(A, B))  
#  print(quotient(A, B)) 
# if __name__ == "__main__":
#     main()
############ EXE 6 : # Avec une lambda, calculer : 
#        #• le cube d’un nombre 
#        #• la somme de deux nombres 
#        #• la valeur absolue d’un nombre 
# y = int (input("Entrez un nombre:"))
# z = float (input("le duexieme nombre :"))
# cube = lambda y : y ** 3
# somme = lambda y, z : y + z
# absolue = lambda z : z if z >= 0 else -z
# print(cube(y))
# print(somme(z, y))
# print(absolue(z))
############ EXE 7 : #Créer une liste de tuples : 
# etudiants = [("Ali", 14),..., ("Taha", 16)] 
# → Trier cette liste du plus grand au plus petit à l’aide de lambda et sorted(). 
# etudiants = [("Ali", 14), ("Ayoub", 18), ("Omar", 10), ("Taha", 16)]
# etudiants_tries = sorted(etudiants, key=lambda x: x[1], reverse=True)
# # print(etudiants_tries)
# for nom, note in etudiants_tries:
#       print(f"{nom} → {note}")
##########################################    list(en python) //tableau (en algoritheme)
# # # 9 — Les Tableaux (Listes) en Python
#    # En Python, on n’utilise pas le mot “tableau” comme en algorithmique classique. 
#     # Le type équivalent s’appelle list (liste). 
#      #  C’est une collection ordonnée et modifiable d’éléments. 
# Syntaxe :  
# nom_liste = [valeur1, valeur2, valeur3, ...] 
##list = [2, 32, 1270, 30743, "holako", "Mohamed", "ben ali"]
# #Chaque élément a un indice (index), qui commence à 0. 
# nombres = [10, 20, 30, 40] 
# print(nombres[0])  # affiche 10 
# print(nombres[3])  # affiche 40
# #⃣ Modification d’un élément 
# nombres[2]="13/12/2025"
# print(nombres)
# #Ajouter :  
# nombres.append('easy')        # ajoute à la fin : AJOUT numbres, str...
# nombres.insert(0, 19.75)    # insère à la position 0 (selon index)
# print(nombres)
# #Supprimer : 
# nombres.remove(40)   # supprime la valeur 40
# del nombres[3]        # supprime l’élément à l’index 3
# nombres.pop()         # supprime le dernier élément 
# print(nombres)
# #Longueur d’une liste  
# print (len(nombres))
# ### p: 21
# #⃣ Parcourir une liste avec une boucle 
# nombres = [5, 10, 15, 20] 
# for n in nombres:  
#     print(n) 
# #Exemple 2 : avec les indices
# for i in range(len(nombres)): 
#    print(f"Élément {i} = {nombres[i]}") 
# #7⃣ Exemple pratique — somme des éléments d’une liste  
# nombres = [2, 4, 6, 8] 
# somme = 0
# for n in nombres: 
#   somme += n 
# print("Somme =", somme)
# #⃣ Remplissage d’une liste à partir du clavier 
# list_vide = []
# somme = 0
# votre_liste = int(input("Entrez des nombre à votre choix:"))
# for i in range(votre_liste):
#     val = int(input(f"entre {i + 1}:"))
#     somme += val
#     list_vide.append(val)
# print("listeeee=",list_vide)
# print("la somme de cette liste est: ", somme)

###### Exemple comlete d'une liste :
# list_nwassa = ["sahla","saha", 1 , 2]
# print(list_nwassa[0])
# print(list_nwassa)
# list_nwassa.pop()
# del list_nwassa[0]
# list_nwassa.remove(1)
# print(list_nwassa)
# list_nwassa.append("daym lah")
# list_nwassa.insert(2, 18)
# print(list_nwassa)
#############
# fruits = ["banane", "remane", "tefah", "adil"]
# for i in fruits:
#     print(f"I like {i}")
##########################
# fruits = ["banane", "remane", "tefah"]
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}- I like {fruit}")
#     print("HOHO")
############################# ⃣ Fonctions utiles sur les listes 
# ##### Exemple comlete d'une liste :
# list_nwassa = ["sahla","saha", 1 , 2]
# print(list_nwassa[0])
# print(list_nwassa)
# list_nwassa.pop()
# del list_nwassa[0]
# list_nwassa.remove(1)
# print(list_nwassa)
# list_nwassa.append("daym lah")
# list_nwassa.insert(2, 18)
# print(list_nwassa)
# print(len(list_nwassa))

# ###########  � Exemple complet 
# #Lire 5 notes, afficher : 
# #• la liste des notes, 
# #• la moyenne, 
# #• la note max et min. 
# notes = [] 
# for i in range(5): 
#      n = float(input(f"Note {i+1} : ")) 
#      notes.append(n)   
# print("Notes :", notes) 
# print("Moyenne :", sum(notes) / len(notes)) 
# print("Max :", max(notes)) 
# print("Min :", min(notes))
# ##########     � Les matrices (tableaux à deux dimensions) 
# ###### Une matrice est une liste de listes. 
#Exeple
# matrice = [ 
# [1, 2, 3], 
# [4, 5, 6], 
# [7, 8, 9] 
# ] 
# print(matrice)
# #Accès à un élément : 
# print(matrice[0][2])  # Element : 3 
#Parcours complet : 
# for i in range(3): 
#   for j in range(3): 
#    print(matrice[i][j], end=" ") 
#   print() 


#######Exercice 2 
# #Lire 5 noms et les afficher dans l’ordre inverse. 
# noms = []
# for i in range(5):
#      tel = int(input(f"nome {i+1} : ")) 
#      noms.append(tel) 
# print(sorted(noms))     #print(list(reversed(noms)))
# noms.reversed()
# print(noms)
# ###########Exercice 3 
# # #Créer une liste et afficher seulement les éléments pairs.  
# N = [0, 1, 2, 5, 6, 7, 20, 60, 91]
# for i in N:
#        if i % 2 == 0 :
#         print(i)
#        # print(f"{i}",  end="\n")
#######    Exercice 4 
# Créer une liste de N nombres, puis afficher le plus grand et le plus petit. 
# N = int(input("Entrez le nombre d'éléments à votre choix : "))
# nombre = []
# for i in range(N):
#      valeur = int(input(f"Le nombre {i+1} :"))
#      nombre.append(valeur)
# print("la liste est :",nombre )   #{i}, #
# ############### Exercice 5 
# #Créer une matrice 3×3 (saisie clavier) et afficher : 
# #• tous les éléments, 
# #• la somme de tous les éléments, 
# #• et la diagonale principale.
# matrice = [ 
# [55, 25, 13, 68], 
# [0, 15, 6, 43], 
# [71, 80, 9,65],
# [34, 1, 28, 54]
# ] 
# for i in range(4):
#    for j in range(3):
#       print(matrice[i][j], end=" ")  #end="\t":tableau  #end="\n\n": deux ligne #end="":no espace #end="_-": tiret
#    print()
# somme = sum(sum(i) for i in matrice)
# print("Somme de la matrice =", somme)
# La deuxieme methodes 
# #somme = 0
# #for ligne in matrice:
# #    for valeur in ligne:
# #        somme += valeur
# print("Somme de la matrice =", somme)
# print(matrice[2][0])
# # afficher la diagonale principale 
# print("Diagonale principale :", [matrice[i][i] for i in range(3)])
# #############
# #### 10 — Les chaînes de caractères (Strings) 
# ## Une chaîne de caractères (ou string) est une suite de caractères : lettres, chiffres, symboles, etc. 
# ## Exemples : 
# "Bonjour", 'Python', "123", 'A'
# ##3⃣ Concaténation (assemblage de chaînes) 
# prenom = "Abderrahman" 
# nom = "Salhi" 
# message = "Bonjour " + prenom + " " + nom 
# print(message)
# ##4⃣ Longueur d’une chaîne
# print(len(message)-len("bonjour  "))
# print(len(prenom))
# print(len(nom))
# #Accès à un caractère (indexation)
# print(nom[1])
# print(nom[-1])   #- Les indices négatifs (nom[-1]) permettent d’accéder depuis la fin.
# ##6⃣ Parcourir une chaîne 
# for i in message :
#   print(i)
#  ##6⃣ Parcourir une chaîne 
# mot = "Python" 
# for c in mot: 
#   print(c)
# ##Extraire une partie de chaîne (Slicing) 
# mot = "Programmation" 
# print(mot[2:4])   # Du 3ᵉ caractère (index 2) jusqu’à l’index 4 exclu
# print(mot[2:])    # à partir de l’indice 2 jusqu’à la fin
# print(mot[:2])     # du début jusqu’à l’indice 2 (exclu) = (مستثنى)

# ##️⃣ Transformation de texte 
# mot = "Programmation" 
# mot = mot.upper()
# print(mot)
# mot= mot.lower() 
# print(mot)
# mot= mot.capitalize() 
# print(mot)
# mot= mot.title() 
# print(mot)
# # 
# print("Bonjour".upper())
# print("Bonjour".lower())
# print("Bonjour".capitalize())
# print("python hola ".strip())
# print("Bonjour".replace("jour", "soir")) # "Bonsoir"

# ##Recherche dans une chaîne
# phrase = "Python est  1 puissant" 
# print("Python" in phrase)      # True 
# print("Java" in phrase)       # False
# print("1" in phrase)         # True 
# ##Pour trouver la position : 
# phrase = "Python est  1 puissant"
# print(phrase.find("est"))   # renvoie 7 

# ##Lecture et affichage formaté 
# ##Exemple 1 : 
# nom = input("Entrez votre nom : ") 
# print("Bonjour", nom) 
# ##Exemple 2 (concaténation formatée) : 
# nom = str(input("Entrez votre nom si vous plais : "))
# age = int(input("Entrez votre age si vous plais : "))
# print(f"Bonjour {nom}, tu as {age} ans.") 
# #Le f"" permet d’insérer des variables dans une chaîne facilement. 

# ##Exemple pratique complet 
# Lire un prénom et un nom, puis : 
# 1. afficher la longueur du nom complet 
# 2. afficher le tout en majuscules 
# 3. afficher seulement le prénom 
# nom = str(input("Entrez votre nom si vous plais : "))
# prenom = (input("Entrez votre prenom si vous plais : "))
# nom_complet = nom + prenom
# print(len(nom_complet))
# print(nom_complet.upper())
# print("Le nom complet est: ", nom_complet)
# print(prenom)
# #Exercices d’application 
# ##Exercice 1 
# Lire une phrase et afficher : 
# • le nombre de caractères, 
# • le premier et le dernier caractère. 
# phrase = "Python est  1 puissant" 
# print(len(phrase))
# print(phrase[0])
# print(phrase[-1]) 
# ##Exercice 2 
# ##Lire une chaîne et l’afficher en majuscules et en minuscules. 
# chaine_caractere = str(input("Entrez une phrase à votre choix : "))
# print(chaine_caractere.upper())
# print(chaine_caractere.lower())
##Exercice 3
##Lire un mot et vérifier s’il contient la lettre 'a'. 
# mot = input("Entrez un mot : ")
# print("a" in mot)
##
# if 'a' in mot:
#     print("Le mot contient la lettre 'a'.")
# else:
#     print("Le mot ne contient pas la lettre 'a'.")
######
# ##Exercice 4 
# ##Créer un tuple de mots et afficher chaque mot avec sa longueur. 
# atuple = ("akhebach", "mohe", "aha", "anzar")
# for n in atuple :
#     print(f"len de {n} : {len(n)}")
# # #Exercice 5 
# #Créer un tuple d’étudiants sous forme : 
# #("Ali", 15), ("Taha", 18), ("Omar", 13) 
# #Puis afficher le nom de l’étudiant qui a la meilleure note. 
# students = (("Ali", 15), ("Taha", 18), ("Omar", 13))
# best_student = max(students, key=lambda x: x[1])
# print("L'étudiant avec la meilleure note est :", best_student[0])

# #Autre methode avec la boucle for :
# etudiants = (("Ali", 15), ("Taha", 18), ("Omar", 13))
# best_nom = " "
# best_note = 0
# for nom, note in etudiants:
#     if note > best_note:
#         best_note = note
#         best_nom = nom 
# print(f"L’étudiant qui a la meilleure note est {best_nom} avec {best_note}")
# ##Les Ensembles (set)
# # Un ensemble (set) est une collection non ordonnée et sans doublons.
# # Modifiable (on peut ajouter ou supprimer des éléments) 
# # Très utile pour les opérations d’ensemble (union, intersection, etc.) 
# # Déclaration d’un ensemble
# #Syntaxe :  
# mon_ensemble = {val1, val2, val3}
# nombres = {10, 20, 30, 40} 
# fruits = {"pomme", "banane", "orange"} 
# vide = set(1 , 2, 44 , 44, 89) 
# print(vide)
# #Test d’appartenance  
# fruits = {"pomme", "banane", "orange"} 
# print("pomme" in fruits)   # True 
# print("fraise" in fruits)   # False 
# #Ajouter :  
# fruits = {"pomme", "banane", "orange"} 
# fruits.add("rmane")
# fruits.add("kiwi")
# print(fruits) 
# #Supprimer : 
# fruits = {"pomme", "banane", "orange"} 
# fruits.remove("banane")   # Erreur si l’élément n’existe pas 
# fruits.discard("pomme")   # Pas d’erreur si l’élément n’existe pas 
# print(fruits) 
# Vider complètement : 
# fruits = {"pomme", "banane", "orange"} 
# fruits.clear() 
# print(fruits)  # set()
# #3Parcourir un ensemble  
# nombres = {10, 20, 30} 
# for n in nombres:        #L’ordre d’affichage peut changer a chaque execution
#     print(n)      
# #Opérations sur les ensembles 
# # Union (∪) 
# a = {1, 2, 3} 
# b = {3, 4, 5} 
# print(a.union(b)) 
# print(a | b)  # {1, 2, 3, 4, 5}  #→ combine deux ensembles (sans doublons) 
# # ##Intersection (∩) 
# print(a.intersection(b))
# print(a & b)  # {3}   #→ éléments communs aux deux ensembles 
# # #Différence (A − B) 
# print(a.difference(b))
# print(a - b)  # {1, 2}   #→ éléments de A qui ne sont pas dans B
# # #Différence symétrique 
# print(a.symmetric_difference(b))
# print(a ^ b)  # {1, 2, 4, 5}  #→ éléments présents dans A ou B mais pas dans les deux 

#            #Fonctions utiles
# | **Fonction** | **Description**               | **Exemple**        | **Résultat**    |
# |--------------|-------------------------------|--------------------|---------------- |
# | `len(s)`     | Nombre d’éléments             | `len({1,2,3})`     | `3`             |
# | `max(s)`     | Plus grand élément            | `max({5,9,2})`     | `9`             |
# | `min(s)`     | Plus petit élément            | `min({5,9,2})`     | `2`             |
# | `sum(s)`     | Somme des éléments            | `sum({2,3,4})`     | `9`             |
# | `s.pop()`    | Supprime un élément au hasard | `{1,2,3}.pop()`    |(résultat dépend)|
# #Des exemples d'utilisations :
# s = { 1, 2, 3} 
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))
# s.pop()
# print(s)
#  #Conversion entre listes, tuples et ensembles 
# #Liste → Ensemble (pour supprimer les doublons) : 
# liste  = [1, 3, 77, 83, 2568]
# ens = set(liste)
# print(liste)
# print(ens)    {1, 3, 2568, 77, 83}    #ne sont pas ordonée
# #Ensemble → Liste :
# ens = {1, 32, 76, 8723}
# liste = list(ens)
# print(ens)
# print(liste) [32, 1, 8723, 76]    #ne sont pas ordonée
# #Exemple complet  
# A = {1, 2, 3, 4} 
# B = {3, 4, 5, 6} 
# print("A ∪ B =", A | B) 
# print("A ∩ B =", A & B) 
# print("A - B =", A - B) 
# print("A Δ B =", A ^ B) 
# A.add(10) 
# B.discard(5) 
# print("A =", A)
#Exercices d’application ✅ 
# #Exercice 1 : # #Créer un ensemble de nombres et afficher :  • sa taille, son maximum et minimum. ✅ 
# Exercice 2  Créer deux ensembles et afficher : leur union, leur intersection. ✅ 
# Exercice 3 Créer une liste avec des doublons et la convertir en ensemble. ✅ 
# Exercice 4 Créer un ensemble de mots et vérifier si un mot donné est présent. ✅ 
# Exercice 5 Soient deux ensembles : 
# A = {2, 4, 6, 8} et B = {4, 8, 12, 16} 
# Afficher : les éléments communs, les éléments différents, les éléments présents seulement dans A ✅ 
# #Les Dictionnaires en Python
# #Un dictionnaire est une collection non ordonnée d’éléments sous forme de paires clé → valeur. 
# NB # une clé (unique) 
#  # une valeur (qui peut être de n’importe quel type)
# #Syntaxe :  
# mon_dico = { 
#        "clé1": valeur1, 
#        "clé2": valeur2, 
#        "clé3": valeur3 }
# # #3 EXEMPLE
# #notes = {"math": 15, "physique": 12, "python": 18} 
# #vide = {}
# etudiant = { 
#           "nom": "Ali", 
#           "age": 20, 
#           "filiere": "Informatique" }
# #Accès aux valeurs 
# #Par la clé :  
# print(etudiant["nom"])    # Ali 
# print(etudiant["filiere"]) # Informatique 
# Si la clé n’existe pas → KeyError. 
# Méthode plus sûre :  
# print(etudiant.get("prenom" , "non precise"))
# print(etudiant.get("ville", "Non précisé")) 
# ## 
# # #Modifier :  
# etudiant["age"] = 21 
# print(etudiant)
# # #Ajouter : 
# etudiant["ville"] = "Casablanca" 
# print(etudiant)
# #  #Supprimer une clé  
# del etudiant["filiere"] 
# print(etudiant)        
# #Ou bien : 
# etudiant.pop("age")
# print(etudiant)
##################
# ##Parcourir un dictionnaire 
# etudiant = { 
#           "nom": "Ali", 
#           "age": 20, 
#           "filiere": "Informatique" }
# # ##Parcourir les clés :  
# for cle in etudiant: 
#        print(cle) 
# # ##Parcourir les valeurs : 
# for valeur in etudiant.values(): 
#    print(valeur) 
# # ##Parcourir les deux : 
# for cle, valeur in etudiant.items(): 
#      print(cle, "-->", valeur)
#   # #Taille du dictionnaire  
# print(len(etudiant))     # Nombre de paires clé/valeur
# # # vide le dictionnaire
# etudiant.clear() 
# print(etudiant)  
# Fonctions et méthodes utiles

# #| Méthode        | Description                          | Exemple             | Résultat                |
# #|----------------|--------------------------------------|---------------------|-------------------------|
# #| d.keys()       | renvoie toutes les clés              | etudiant.keys()     | dict_keys([...])        |
# #| d.values()     | renvoie toutes les valeurs           | etudiant.values()   | dict_values([...])      |
# #| d.items()      | renvoie les couples (clé, valeur)    | etudiant.items()    | dict_items([...])       |
# #| d.clear()      | vide le dictionnaire                 | —                   | —                       |
# #| del d["clé"]   | supprime une entrée                  | —                   | —                       |
# #| "clé" in d     | test d’existence                     | "nom" in etudiant   | True                    |

# #Exemple complet   d.keys d.values d.items
# etudiant = { 
# "nom": "Ayoub", 
# "age": 22, 
# "filiere": "IA", 
# "note": 17.5 } 
# print("Nom :", etudiant["nom"]) 
# print("Âge :", etudiant["age"]) 
# print("Filière :", etudiant["filiere"]) 
# print("Note :", etudiant["note"]) 
# etudiant["ville"] = "Tamesna" 
# etudiant["note"] = 18 
# print("\nAprès mise à jour :", etudiant) 
# print("\nToutes les clés :", etudiant.keys()) 
# print("Toutes les valeurs :", etudiant.values()) 
# for cle, valeur in etudiant.items(): 
#    print(f"{cle} : {valeur}")
###############
# # Dictionnaire de dictionnaires 
# # Un dictionnaire peut contenir d’autres dictionnaires 
# etudiants = { 
# "E1": {"nom": "Ali", "age": 20, "note": 15}, 
# "E2": {"nom": "Sara", "age": 22, "note": 17}, 
# "E3": {"nom": "Omar", "age": 21, "note": 14} } 
# print(etudiants["E2"]["nom"])  # Sara 
#############   Exercices d’application 
# #Exercice 1 
# # Créer un dictionnaire personne avec les clés : nom, âge, ville, Afficher ses informations. 
# personne = {
#     "nom" : "Mohamed",
#     "age" : 20,
#     "ville" : "Errachidia"
#     }
# print(personne)
# #Exercice 2 
# # Ajouter une nouvelle clé profession et modifier la clé ville.
# personne["profession"] = "etudiant"
# personne["vlle"] = "Morroco"
# print(personne)
# #Exercice 3 
# #Créer un dictionnaire de 3 étudiants avec leur note, puis : 
# #afficher la moyenne  afficher le nom de l’étudiant ayant la meilleure note 
# etudiants = {
#     "Ali": [14, 19, 20],
#     "Sara": [18, 17, 19],
#     "Youssef": [12, 15, 19]
#      }
# for nom, note in etudiants.items() :
#     moyenne = sum(note) / len(etudiants)
#     print(f"la moyenne de {nom} est {moyenne:2f}")
# meilleur_etudiant = max(etudiants, key=etudiants.get)
# print(f"Meilleure note : {etudiants[meilleur_etudiant]} (attribuée à {meilleur_etudiant})")
#############
# #Création du dictionnaire représentant le stock
# stock = {
#     "pomme": 50,
#     "banane": 30,
#     "orange": 20   }
# # Ajouter un nouveau produit
# stock["fraise"] = 40   # ajout d'un produit avec sa quantité
# # Retirer un produit
# del stock["banane"]    # suppression d'un produit
# # Afficher le total d’articles en stock
# total = sum(stock.values())
# print("Stock actuel :", stock)
# print("Total d’articles en stock :", total)

########### Exercice 4
# # Création du dictionnaire de notes
# etudiants = {
#     "Ali": [12, 15, 14],
#     "Sara": [18, 17, 19],
#     "Youssef": [10, 12, 11],
#     "Mouna": [16, 14, 15]  }
# # Calcul et affichage de la moyenne pour chaque étudiant
# for nom, notes in etudiants.items():
#     moyenne = sum(notes) / len(notes)
#     print(f"{nom} → Moyenne : {moyenne:.2f}")
##############
# # 14 — Les Bibliothèques Standards en Python
# # 1⃣ Qu’est-ce qu’une bibliothèque (ou module) ?
# # Une bibliothèque (appelée aussi module) est un ensemble de fonctions et outils prêts à l’emploi. 
# # Elle permet d’éviter de tout réécrire soi-même. 
# # Python fournit plus de 200 modules standards déjà inclus. 


# # Fonctions du module math

# | Fonction        | Description           | Exemple        | Résultat   |
# |-----------------|-----------------------|----------------|------------|
# | math.sqrt(x)    | racine carrée         | math.sqrt(9)   | 3.0        |
# | math.pow(a, b)  | puissance             | math.pow(2, 3) | 8.0        |
# | math.ceil(x)    | arrondi supérieur     | math.ceil(2.3) | 3          |
# | math.floor(x)   | arrondi inférieur     | math.floor(2.9)| 2          |
# | math.pi         | nombre π              | —              | 3.14159    |
# | math.sin(x)     | sinus (en radians)    | math.sin(math.pi/2) | 1.0   |
###############
# # Exemple complet 
# import random 
# liste = ["Ali", "Sara", "Omar", "Salma"] 
# print("Nom choisi :", random.choice(liste)) 
# print("Nombre entre 1 et 10 :", random.randint(1, 10)) 
################
# #d) Module os — Système d’exploitation 
# #Permet d’interagir avec les fichiers et dossiers. 
# import os 
# print(os.getcwd())     # répertoire actuel 
# # os.mkdir("dossier")  # créer un dossier 
# # os.remove("fichier.txt")  # supprimer un fichier
################
# import os
# # #عرض المجلد الحالي
# print("Répertoire actuel:", os.getcwd())
# # #إنشاء مجلد جديد
# #os.mkdir("nouveau_dossier")
# # #عرض المحتويات بعد الإنشاء
# print("Contenu:", os.listdir())
##############
# # os.mkdir("dossier")  # créer un dossier 
# # os.remove("fichier.txt")  # supprimer un fichier 
##############
# #e) Module sys — Système Python 
# # Permet d’interagir avec l’interpréteur Python. 
# import sys 
# print("Version de Python :", sys.version)
##############
# # f) Module time — Mesure du temps  
# import time 
# print("Heure actuelle :", time.ctime()) 
# time.sleep(10)   # pause de 2 secondes 
# print("Reprise du programme")
############## 
# # g) Module datetime — Date et heure avancées
# import datetime 
# maintenant = datetime.datetime.now() 
# print("Date et heure actuelles :", maintenant) 
# aujourdhui = datetime.date.today() 
# print("Date du jour :", aujourdhui) 
# # # Exemple : extraire jour, mois, année
# from datetime import date 
# anniversaire = date(2000, 5, 10) 
# print("Anniversaire :", anniversaire) 
# print("Année :", anniversaire.year) 
# print("Mois :", anniversaire.month) 
# print("Jour :", anniversaire.day) 
# ##############
# # 4⃣ Exemple combiné  
# import math, random, datetime 
# r = random.randint(1, 10) 
# aire = math.pi * r**2 
# print("Rayon :", r) 
# print("Aire du cercle :", round(aire, 2)) 
# print("Calcul effectué le :", datetime.date.today()) 
##############
# # Autres modules utiles à connaître 
## | Module      | Utilité principale                                       |
## |-------------|----------------------------------------------------------|
## | statistics  | Calculs statistiques (moyenne, médiane, etc.)            |
## | json        | Lecture/écriture de fichiers JSON                        |
## | csv         | Lecture/écriture de fichiers CSV                         |
## | re          | Expressions régulières (recherche dans texte)            |
## | collections | Outils avancés pour les listes et dictionnaires          |
## | math        | Fonctions mathématiques                                  |
## | Module      | Utilisation principale                                   |
## |-------------|----------------------------------------------------------|
## | datetime    | Gestion du temps                                         |   
## | os, sys     | Interaction avec le système                              |
## | random      | Tirages aléatoires                                       |
## | time        | Mesure et attente                                        |
############# Exemples d’utilisation
# # Exemple avec statistics :
# import statistics
# data = [10, 20, 30, 40]
# print(statistics.mean(data))   # 25
# print(statistics.median(data)) # 25
# print(statistics.mode(data)) # 10
# print(statistics.stdev(data)) # 12.909944487358056 
#############
# import json
# person = {"name": "Mohamed", "age": 25}
# json_str = json.dumps(person)   # تحويل إلى نص JSON
# print(json_str)
#######
# import csv
# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["الاسم", "العمر"])
#     writer.writerow(["محمد", 25])
############## 
# import re
# text = "Python قوي ومفيد وسهل"
# result = re.findall(r"\b[أ-ي]\w+", text)
# print(result)
##############
# import collections    
# # counter = collections.Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
# # print(counter)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})   
# from collections import Counter
# from collections import deque
# data = ["a", "b", "a", "c", "b", "a"]
# print(deque(data))  # Counter({'a': 3, 'b': 2, 'c': 1})
###############
# import math
# print(math.sqrt(16))   # 4.0              
# print(math.pi)         # 3.141592653589793
############## Exercices d’application ✅
## Exercice 1  Utiliser le module math pour calculer : 
## • la racine carrée de 81 • l’arrondi supérieur et inférieur de 5.7 
## • le sinus de 90° (convertir en radians : math.radians(90))  
# import math 
# racine_caree = math.sqrt(81)
# arrondi_superieur = math.ceil(5.7)
# arrondi_inferieur = math.floor(5.7)
# sin= math.sin(90)
# # sinus_90 = math.sin(math.radians(90))
# print("Racine carrée de 81 :", racine_caree)
# print("Arrondi supérieur de 5.7 :", arrondi_superieur)      
# print("Arrondi inférieur de 5.7 :", arrondi_inferieur)
# print("sin de 90 :", sin)
# # print("Sinus de 90° :", sinus_90)
############## Exercice 2  Afficher la date et l’heure actuelles avec datetime. 
# import datetime
# maintenant = datetime.datetime.now()
# print("Date et heure actuelles :", maintenant)
# ############# Exercice 3  Utiliser le module random pour :
# # Tirer un nombre aléatoire entre 1 et 100 jusqu’à obtenir 50. Compter le nombre d’essais.
# # # la premiere methode  
# import random
# nombre_cible = 50
# essais = 0      
# while True:
#     nombre_aleatoire = random.randint(1, 100)
#     essais += 1
#     if nombre_aleatoire == nombre_cible:
#         break       
# print(f"Nombre {nombre_cible} obtenu après {essais} essais.")
# # la deuxieme methode
# import random
# # Initialisation
# essais = 0
# nombre = 0
# # Boucle jusqu'à obtenir 50
# while nombre != 50:
#     nombre = random.randint(1, 100)  # Tirage aléatoire
#     essais += 1
# print(f"Nombre obtenu : {nombre}")
# print(f"Nombre d'essais : {essais}")
############ Exercice 4  Exercice 4 
# #Créer un petit programme qui affiche : Aujourd’hui, nous sommes le <jour>/<mois>/<année> 
# import datetime as dt
# aujourdoui = dt.datetime.today()
# jour = aujourdoui.day
# mois = aujourdoui.month 
# annee = aujourdoui.year
# print(f"Aujourd’hui, nous sommes le {jour}/{mois}/{annee}")
# print(aujourdoui.strftime("Aujourd’hui, nous sommes le %d/%m/%Y"))
# ############ Exercice 5 Exercice 5 (défi) 
## 1. tire un nombre aléatoire entre 1 et 10 
## 2. demande à l’utilisateur de le deviner
## 3. indique s’il a gagné ou non (utiliser random et une boucle)
# import random
# nombre_secret = random.randint(1, 10)       
# essai = 0
# trouve = False  
# while not trouve:
#     essai = int(input("Devine le nombre (entre 1 et 10) : ")) 
#     if essai == nombre_secret:
#         print("Bravo 🎉 ! Tu as trouvé le bon nombre :", nombre_secret)
#         trouve = True
#     else:
#         print("Raté 😅, essaie encore...") 
######################################
# # # 15 — Les Fichiers en Python
# # Écriture
# f = open("notes.txt", "w")
# f.write("Bonjour Mohamed !\n")
# f.close()
# # Lecture
# f = open("notes.txt", "r")
# contenu = f.read()
# print(contenu)
# f.close()
# # Ajout 
# with open("notes.txt", "a") as f:
#     f.write("Encore une ligne ajoutée.\n")
# # Lecture avec contexte
# with open("notes.txt", "r") as f:
#     print(f.read())
############# exemple d'utilisation :
# # Écriture
# f = open("test.txt", "w") 
# f.write("Bonjour Python !") 
# f.close() 
#  # Lecture
# f = open("test.txt", "r") 
# contenu = f.read()  
# print(contenu)
# f.close()
# # Ajout
# f= open("test.txt", "a") 
# f.write("\nBienvenue dans le monde des fichiers.")      
# f.close()  
# # Lecture avec contexte 
# with open("test.txt", "r") as f: 
#     print(f.read()) 
# ########### Exercices d’application ✅
# f = open("exemple.txt", "w")
# f.write("all ah y3awnkom alhamdolilah\n youma 3andna cours python\n fuck hwo hate us ")
# f.close()         
# # read              
# f = open("exemple.txt", "r" )
# contenu = f.read()
# print(contenu)
# f.close()

# # #3 ⃣ Écrire dans un fichier 
# # # a) Écrire une seule ligne  
# f = open("exemple.txt", "w") 
# f.write("Ceci est la première ligne.\n") 
# f.write("Et voici une autre.\n") 
# f.close() 
# # b) Écrire plusieurs lignes avec writelines() 
# lignes = ["Ligne 1\n", "Ligne 2\n", "Ligne 3\n"] 
# f = open("multi.txt", "w") 
# f.writelines(lignes) 
# f.close() 
    
# # Lire un fichier 
# # a) Lire tout le contenu  
# f = open("exemple.txt", "r") 
# contenu = f.read() 
# print(contenu) 
# f.close() 
# # b) Lire ligne par ligne 
# f = open("exemple.txt", "r") 
# for ligne in f: 
#  print(ligne.strip())  # strip enlève le saut de ligne 
# f.close() 
# # c) Lire une seule ligne 
# f = open("exemple.txt", "r") 
# print(f.readline())  # lit une ligne 
# f.close() 
############## # # Vérifier si un fichier existe
# import os 
# if os.path.exists("notes.txt"): 
#     print("Le fichier existe") 
# else: 
#      print("Fichier introuvable") 
# ############# Ajouter du contenu à la fin d’un fichier  
# f = open("exemple.txt", "a") 
# f.write("Nouvelle ligne ajoutée !\n") 
# f.close() 
############# Fermer un fichier 
# f.close()
#############     Utiliser with open(...) (méthode recommandée) 
# # ecriture
# with open("data.txt", "w") as f: 
#   f.write("Python est génial !") 
# # lecture premiere methode  
# with open("data.txt", "r") as f: 
#    contenu = f.read() 
#    print(contenu) 
# # deuxieme methode de lecture
# with open("data.txt", "r") as f: 
#   print(f.read())
############## ⃣ Exemple complet  
# Création du fichier 
# with open("notes.txt", "w") as f: 
#     f.write("Note 1 : 15\n") 
#     f.write("Note 2 : 18\n") 
# Lecture du fichier 
# with open("notes.txt", "r") as f: 
#     lignes = f.readlines() 
#     for l in lignes: 
#        print(l.strip())
################ Vérifier si un fichier existe  
# import os 
# if os.path.exists("notes.txt"): 
#     print("Le fichier existe") 
# else:  
#     print("Fichier introuvable")
################  Lire ou écrire des fichiers CSV 
# # Fichiers CSV = fichiers texte avec des données séparées par des virgules (souvent utilisés avec Excel). 
# import csv 
# # Écriture 
# with open("etudiants.csv", "w", newline="") as f: 
#      writer = csv.writer(f) 
#      writer.writerow(["Nom", "Note"]) 
#      print("Fichier CSV créé avec succès.")
#      writer.writerow(["Ali", 17]) 
#      writer.writerow(["Sara", 15]) 
# # # Lecture 
# with open("etudiants.csv", "r") as f: 
#      lecteur = csv.reader(f) 
#      for ligne in lecteur: 
#        print(ligne)
################  Exercices pratiques 
## Exercice 1 / Créer un fichier bonjour.txt et y écrire : 
##  Bonjour 
##  Je découvre la gestion des fichiers en Python 
# with open("bonjour.txt", "w") as f:
#     f.write("Bonjour\n")  
#     f.write("Je découvre la gestion des fichiers en Python\n")
# print("Fichier bonjour.txt créé avec succès.")             
# Exercice 2 / Lire le fichier bonjour.txt et afficher son contenu.
# # premiere methode : 
# with open("bonjour.txt", "r") as f:
#     contenu = f.read()
#     print(contenu)
## deuxieme methode :           #### conlusion : plusieurs methodes pour lire un fichier
# with open("bonjour.txt", "r") as f :             ##✅ Conclusion
#     for  ligne in f:               ## - Méthodes qui affichent ligne par ligne :
#         print(ligne.strip())       ## - Deuxième méthode (avec for ligne in f)
## troisieme methode:               ## - Troisième méthode (avec for ligne in f + f.close())
# #  close maniuelle                 ## - Méthodes qui affichent tout le fichier d’un coup :
# f = open("bonjour.txt", "r")       ## - Première méthode (f.read())
# for ligne in f:                    ## - Quatrième méthode (f.read())
#     print(ligne.strip())           
# f.close() 
## quatrieme methode :
# with open("bonjour.txt", "r") as f :
#   print(f.read())
############ Exercice 3  Ajouter à la fin du fichier la phrase : 
"C’est facile d’écrire dans un fichier !"
# with open("bonjour.txt", "a") as f :
#     f.write("C'st facile d'ecrire dans un fichier !\n")
#     print("Phrase ajoutée avec succès.")
############ Exercice 4 
##Créer un fichier nombres.txt contenant les nombres de 1 à 10 (un par ligne). 
# with open("nombre.txt", "w") as f :
#     for i in range (1,11):
#         f.write(f"{i}\n")
#     print("Fichier nombres.txt créé avec succès.")
############ Exercice 5 
## Lire le fichier nombres.txt, calculer la somme de tous les nombres et afficher le résultat. 
# with open("nombre.txt", "r") as f:
#     total = 0
#     for ligne in f :
#         somme = int(ligne.strip())
#         total += somme
#     print("La somme des nombres est :", total)
## deuxieme methode :
# total = 0
# f = open("nombre.txt", "r")   
# for ligne in f :
#     somme = int(ligne.strip())
#     total += somme
# print("La somme des nombres est :", total)
# f.close()
##################
###########  Manipulation des fichiers JSON en Python"
# # Exemple d’un fichier etudiant.json :  
# with open("etudiant.json", "w") as f:
#     f.write('{"nom": "Amine", "age": 21, "notes": [15, 18, 17]}')   
# # Lecture du fichier JSON
# import json 
# with open("etudiant.json", "r") as f:
#     etudiant = json.load(f)
#     print(etudiant)
#############     #  Écrire (sauvegarder) des données en JSON 
# On utilise la fonction json.dump() pour écrire dans un fichier. Exemple :  
# import json 
# etudiant = { 
# "nom": "Ali", 
# "age": 20, 
# "notes": [14, 16, 18], 
# "admis": True } 
# with open("etudiant.json", "w") as f: 
#     json.dump(etudiant, f)
## Cela crée un fichier etudiant.json contenant : 
## {"nom": "Ali", "age": 20, "notes": [14, 16, 18], "admis": true} 
## # ecriture avec formatage lisible
# with open("etudiant.json", "w") as f: 
#           json.dump(etudiant, f, indent=4)  # indent pour formatage lisible

# #Résultat : 
# #"{ "nom": "Ali", 
# #"age": 20, 
# #"notes": [14, 16, 18], 
# #"admis": true }"  
## ire (charger) un fichier JSON 
## Pour relire un fichier JSON et récupérer ses données sous forme de dictionnaire Python, on utilise 
## json.load() : 
# import json 
# with open("etudiant.json", "r") as f: 
#      data = json.load(f) 
# print(data) 
# print("Nom :", data["nom"]) 
# print("Moyenne :", sum(data["notes"]) / len(data["notes"])) 




################   
# class CompteBancaire:
#     def __init__(self, titulaire):
#         self.titulaire = titulaire
#         self.__solde = 0
#     def deposer(self, montant):
#         if montant > 0:
#             self.__solde += montant
#         else:
#             print("Montant invalide.")
#     def retirer(self, montant):
#         if montant <= self.__solde:
#             self.__solde -= montant
#         else:
#             print("Solde insuffisant.")
#     def afficher_solde(self):
#         print(f"Solde actuel : {self.__solde} MAD")
#     def __str__(self):
#         return f"Compte de {self.titulaire} – Solde : {self.__solde} MAD"
# # Test
# c1 = CompteBancaire("Mohamed")
# c1.deposer(1000)
# c1.retirer(400)
# c1.afficher_solde()
# print(c1)

############### 
# # Calculs avec NumPy
# arr = np.array([12, 15, 9])
# print("Somme avec NumPy:", np.sum(arr))

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Données avec Pandas
# data = {"Nom": ["Ali", "Sara", "Youssef"], "Note": [12, 15, 9]}
# df = pd.DataFrame(data)
# print("Moyenne des notes avec Pandas:", df["Note"].mean())

# # Calculs avec NumPy
# arr = np.array([12, 15, 9])
# print("Somme avec NumPy:", np.sum(arr))

# # Visualisation avec Matplotlib
# plt.bar(df["Nom"], df["Note"], color="skyblue" )   #hist
# plt.title("Notes des étudiants")
# plt.show()

####################### DE 07/02/2026 à 08/02/2026
# # 16 — Les Bibliothèques Externes en Python
# # 1⃣ Qu’est-ce qu’une bibliothèque externe ?
# # Une bibliothèque externe est un ensemble de fonctions et outils développés par la communauté, qui n’est pas inclus dans la bibliothèque standard de Python.
# # Elles doivent être installées séparément (généralement via pip) avant de pouvoir
# # être utilisées.
# # 2⃣ Comment installer une bibliothèque externe ?
# # La plupart des bibliothèques externes sont disponibles sur le Python Package Index (PyPI) et peuvent être installées avec pip, le gestionnaire de paquets de Python.
# # Commande d’installation :
# # pip install nom_de_la_bibliothèque
# # Exemple : installer la bibliothèque requests pour faire des requêtes HTTP
# # pip install requests    
# # 3⃣ Exemples de bibliothèques externes populaires
# # | Bibliothèque  | Utilité principale                                       |    
# |---------------|----------------------------------------------------------|
# | NumPy         | Calculs numériques avancés (tableaux, matrices, etc.)   |
# | Pandas        | Manipulation et analyse de données                      |
# | Matplotlib    | Visualisation de données (graphiques, plots, etc.)     |
# | Requests      | Faire des requêtes HTTP (API, web scraping)             |
# | BeautifulSoup | Analyse et extraction de données à partir de HTML       |
# # 4⃣ Exemple d’utilisation de NumPy, Pandas et Matplotlib
# import numpy as np    
# import pandas as pd
# import matplotlib.pyplot as plt
# # Création d’un DataFrame avec Pandas
# data = {"Nom": ["Ali", "Sara", "Youssef"], "Note": [12, 15, 9]}
# df = pd.DataFrame(data)
# print("Moyenne des notes avec Pandas:", df["Note"].mean())
# # Calculs avec NumPy
# arr = np.array([12, 15, 9])
# print("Somme avec NumPy:", np.sum(arr))
# # Visualisation avec Matplotlib
# plt.bar(df["Nom"], df["Note"], color="skyblue")
# plt.title("Notes des étudiants")
# plt.show()

# #---------------------------------------------------------------------------------------------------------------------------------------
####################### DE 07/02/2026 à 08/02/2026

########################## LES EXPRESSIONS RÉGULIÈRES (REGEX) ##########################
# import re

# text = "contact@graven.yt"
# pattern = r'^[a-zA-Z0-9_.-]+@[a-z]{2,}+\.+[a-z]{2,}$'  # pattern pour vérifier une adresse email

# text1 = ("contact@graven.yt", "Mohamed@ben&ali.com")
# pattern1 = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'  # pattern pour verefier les deux adresses email

# vérifier si le texte respecte le pattern  
#### methode 1 :
# if re.match(pattern1, text1[0])  and re.match(pattern1, text1[1]):
#     print("Email valide")
# else:
#     print("Email invalide")
#### methode 2 :
# for text in text1:
#     if re.match(pattern1, text):
#         print(f"{text} → Email valide")
#     else:
#         print(f"{text} → Email invalide")

################
# import re
# text = "https://www.youtube.com/channel/UC1234567890"
# pattern = r'^https?://(www\.)?youtube\.com/(channel|user|c)/[A-Za-z0-9_-]+$'   # premeire version du pattern

# # pattern = r'^https?://(www\.)?youtube\.com/channel/[A-Za-z0-9_-]+$'
# #explication du pattern :
# # ^https?:// : commence par http:// ou https://
# # (www\.)? : optionnellement suivi de www.
# # youtube\.com/ : suivi de youtube.com/
# # (channel|user|c)/ : suivi de channel/, user/ ou c/
# # [A-Za-z0-9_-]+ : suivi d'un identifiant composé de lettres, chiffres, tirets ou underscores
# # $ : fin de la chaîne

# # vérifier si le texte respecte le pattern
# if re.match(pattern, text):
#     print("URL YouTube valide")
# else:
#     print("URL YouTube invalide")

##############
# import re
# text = "https://www.youtube.com/watch?v=ABC123xyz"
# pattern = r'^https?://(www\.)?youtube\.com/watch\?v=[A-Za-z0-9-]{9}$'  # pattern pour les liens de vidéos YouTube
# # vérifier si le texte respecte le pattern
# if re.match(pattern, text):
#     print("Lien YouTube valide")
# else:
#     print("Lien YouTube invalide")

##################
# import re

# text = "Passw0rd@2026hG"
# pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$'
# # explication du pattern :
# # ^ : début de la chaîne
# # .* : n'importe quel caractère (sauf \n) zéro ou plusieurs fois
# # (?=.*[A-Z]) : au moins une lettre majuscule
# # (?=.*[a-z]) : au moins une lettre minuscule
# # (?=.*[0-9]) : au moins un chiffre
# # (?=.*[@$!%*?&]) : au moins un caractère spécial parmi @$!%*?&
# # [A-Za-z0-9@$!%*?&-]{8,} : au moins 8 caractères parmi les lettres, chiffres et caractères spéciaux
# # $ : fin de la chaîne
# # vérifier si le texte respecte le pattern
# if re.match(pattern, text):
#     print("Mot de passe valide")
# else:
#     print("Mot de passe invalide")

#################
# import re
# text = "0599123415"
# pattern = r"^(?:.*\+212|0)([5-7][0-9]{8})$"  # pattern pour les numéros de téléphone marocains
# # expliquer le pattern :
# # ^ : début de la chaîne
# # (?:...) : groupe non capturant, utilisé pour regrouper des éléments sans les capturer pour les résultats de recherche
# # (?=.* ): assertion positive, vérifie que le motif à l'intérieur est présent quelque part dans la chaîne # oblgatoire pour les numéros de téléphone marocains d'avoir +212 ou 0 au début du numéro
# # .* : n'importe quel caractère (sauf \n) zéro ou plusieurs fois
# # (?:.*\+212|0) : optionnellement suivi de n'importe quoi puis +212 ou de 0
# # ([5-7][0-9]{8}) : suivi d'un chiffre entre 5 et 7 puis de 8 chiffres
# # $ : fin de la chaîne
# # qeul est le role de.* dans le pattern ?
# # .* : n'importe quel caractère (sauf \n) zéro ou plusieurs fois

# # pattern = r"^0[5-7][0-9]{8}$"  # pattern pour les numéros de téléphone marocains
# if re.match(pattern, text):
#     print("Mot de passe valide")
# else:
#     print("Mot de passe invalide")

####################
# import re
# texte = "Bonjour Mohamed, Bonjour le monde!"

# # 1. search → أول تطابق
# print(re.search(r"Bonjour", texte))  
# # يطبع كائن فيه أول "Bonjour"

# # 2. findall → جميع التطابقات
# print(re.findall(r"Bonjour", texte))  
# # ['Bonjour', 'Bonjour']

# # 3. match → بداية النص فقط
# print(re.match(r"Bonjour", texte))  
# # يطابق لأن النص يبدأ بـ Bonjour

# # 4. split → تقسيم النص
# print(re.split(r"\s", texte))  
# # ['Bonjour', 'Mohamed,', 'Bonjour', 'le', 'monde!']

# # 5. sub → استبدال
# print(re.sub(r"Bonjour", "Salut", texte))  
# # "Salut Mohamed, Salut le monde!"
###############
# import re

# texte = "Le prix est 250 euros pour ce produit."
# # نبحث عن أول رقم داخل النص
# resultat = re.search(r"\d+", texte)
# if resultat:
#     print("Premier nombre trouvé:", resultat)
# else:
#     print("Aucun nombre trouvé")

#################### autre exemple pour re.search
# import re

# texte = "Le prix est 250 euros pour ce produit."
# resultat = re.search(r"\d+", texte)
# print(resultat)          # يطبع الكائن Match object
# print(resultat.group())  # يطبع النص المطابق "250"  # - \d+ → يلتقط الأرقام كاملة (جشع).
# print(resultat.span())   # يطبع (12, 15) أي موقع التطابق -# \d+? → يلتقط الأرقام رقمًا رقمًا (غير جشع)

# #################### en utilisant d+ للبحث عن جميع الأرقام في النص
# import re

# texte = "Prix: 250 euros, code 123"
# print(re.search(r"\d+", texte))       # أول تطابق → Match object
# print(re.findall(r"\d+", texte))      # ['250', '123']
# print(re.match(r"\d+", texte))        # None (لأن النص لا يبدأ برقم)
# print(re.split(r"\d+", texte))        # ['Prix: ', ' euros, code ', '']
# print(re.sub(r"\d+", "yyyy", texte))   # "Prix: yyyy euros, code yyyy"

#####################
# import re

# texte = "Prix: 250 euros et code 123"
# print(re.findall(r"\d+", texte))   # ['250', '123']
# print(re.findall(r"\d+?", texte))  # ['2', '5', '0', '1', '2', '3']

###################### 
# # when add + to \d or \D or \w or \W or \s or \S it becomes greedy and capture as much as possible while when add ? 
# # it becomes non greedy and capture as little as possible
# import re       # # # donc \d+? = \d # d+ يلتقط الأرقام رقمًا رقمًا (غير جشع)
# texte = "Prix: 2-50 euros!"
# print(re.findall(r"\d+", texte))   # ['2','5','0'] # \d+ يلتقط الأرقام كاملة (جشع)
# print(re.findall(r"\D+", texte))   # ['P','r','i','x',':',' ',' ','e','u','r','o','s','!'] # \D+ يلتقط كل شيء ما عدا الأرقام
# print(re.findall(r"\w+", texte))   # ['P','r','i','x','2','5','0','e','u','r','o','s'] # \w+: Underscores يلتقط الحروف والأرقام وال 
# print(re.findall(r"\W+", texte))   # [':',' ',' ','!']  # \W+ : underscores يلتقط كل شيء ما عدا الحروف والأرقام وال 
# print(re.findall(r"\s+", texte))   # [' ', ' ']  # \s+: يلتقط المسافات فقط
# print(re.findall(r"\S+", texte))   # ['P','r','i','x',':','2','5','0','e','u','r','o','s','!'] #  \S+: يلتقط كل شيء ما عدا المسافات
# # # #  \d+ → يلتقط الأرقام كاملة (جشع). # \d+? = \d → يلتقط الأرقام رقمًا رقمًا (غير جشع) split the text into words and numbers.

#####################
# import re
# texte = "Prix: 250 euros et code 123"
# print(re.findall(r"\d+", texte))   # ['250', '123']  ← جشع
# print(re.findall(r"\d+?", texte))  # ['2','5','0','1','2','3'] ← غير جشع

################
# #c) Extraire les mots commençant par une majuscule  
# import re 
# texte = "Ali et Taha apprennent Python à Tamesna" 
# maj = re.findall(r"\b[A-Z][a-z]+", texte) # ['Ali', 'Taha', 'Python', 'Tamesna']
# print(maj) 
################
# #e) Découper une phrase en mots  
# import re 
# phrase = "Bonjour, comment vas-tu ?" 
# mots = re.split(r"\W+", phrase) # ['Bonjour', 'comment', 'vas', 'tu', ''] 
# print(mots)  # en utilisant \W= pour séparer les mots par les caractères non alphanumériques (comme les espaces et la ponctuation)

################
#  #f) Remplacer plusieurs espaces par un seul  
# import re 
# texte = "Python    est   super" 
# texte_nettoye = re.sub(r"\s+", " ", texte) 
# print(texte_nettoye) 

################
# import re 
# # numero = "+212-782281740" 
# numero = "+212612345678"  # +212-612 345678
# pattern = r"^\+212[-\s]?[6-7]\d{2}[-\s]?\d{6}$" # يطابق إما شرطة - أو مسافة \s، والـ ? يعني أن وجودها اختياري (صفر أو واحد).
# if re.match(pattern, numero): 
#    print("Numéro valide") 
# else: 
#     print("Numéro invalide") 

################  EXER 1: Écrire un programme qui extrait tous les nombres d’un texte. 
# import re
# texte = "Le prix est de 250 euros, et le code est 123"
# pattern = r"\d+"    # \d+ يلتقط الأرقام كاملة (جشع)             
# resultats = re.findall(pattern, texte)  # re.findall pour trouver tous الأرقام في النص
# print(resultats)  # ['250', '123']  

# # 2eme méthode pour trouver أول رقم في النص
# import re 
# texte = "Le prix est de 250 euros, et le code est 123"
# pattern = r"\d+"
# resultats = re.search(pattern, texte)
# print(resultats.group())  # يطبع أول رقم "250"

# # 3eme méthode pour trouver le premier nombre dans le texte .
# import re 
# texte = "Le prix est de 250 euros, et le code est 123"
# resultats = re.search(r"\d+", texte)
# print(resultats.group())

######################## Exercice 2 
# #Écrire un programme qui vérifie si un texte commence par "Bonjour"
# import re
# texte = " Bonjour tout le monde!"    
# pattern = r"^\s*Bonjour"  # ^ signifie que le texte doit commencer par "Bonjour"  
# # si il y a un espace avant "Bonjour" le pattern ne va pas marcher parce que le texte ne commence pas par "Bonjour" mais par un espace .
# # pour résoudre ce problème on peut utiliser \s* pour ignorer les espaces au début du texte : pattern = r"^\s*Bonjour"
# if re.match(pattern, texte):
#     print("Le texte commence par 'Bonjour'")
# else:   
#     print("Le texte ne commence pas par 'Bonjour'")
# # 2eme méthode pour vérifier si un texte commence par "Bonjour"
# import re
# # Exemple de texte
# texte1 = "Bonjour tout le monde"
# texte2 = "Salut, Bonjour à toi"
# # Pattern : ^Bonjour → doit commencer par "Bonjour"
# pattern = r"^Bonjour"
# print(bool(re.match(pattern, texte1)))  # True → commence par "Bonjour"
# print(bool(re.match(pattern, texte2)))  # False → ne commence pas par "Bonjour" # bool() pour convertir le résultat en True ou False

################## Exercice 3:
# #Écrire une fonction valide_email(email) qui renvoie True si l’adresse est correcte, sinon False.
# import re 
# texte = "mohamed@gmail.com" 
# patteren3 = r'^\w{2,}@\w{2,}\.com$'
# # patteren = r'^\w+@\w+\.\w+$'  # pattern pour vérifier une adresse email
# # patteren1 = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'  # pattern pour vérifier une adresse email plus robuste
# # patteren2 = r'^[a-zA-Z0-9_.-]+@[a-z]{2,}+\.+[a-z]{2,}$'  # pattern pour vérifier une adresse email plus simple
# if re.match(patteren3, texte):
#     print("Email valide")
# else:
#     print("Email invalide")
########################## Exercice 4:
# import re
# # Exemple de texte
# texte = "Bonjour Mohamed, bienvenue à Rabat avec Ali et Fatima."
# # Regex : \b[A-Z][a-z]+
# mots = re.findall(r"\b[A-Z][a-z]+", texte)
# print(mots) # ['Bonjour', 'Mohamed', 'Rabat', 'Ali', 'Fatima']  # \b : début de mot, [A-Z] : majuscule, [a-z]+ : lettres minuscules

############### # #Exercice 5 :
# #Créer un programme qui vérifie si une date est valide au format JJ/MM/AAAA. 
# import re
# date = "29/02/2024, 30/02/2023, 08/02/2026, 99/99/9999"
# pattern = r"^\d{2}/\d{2}/\d{4}$"  # pattern pour vérifier le format de la date
# dates = date.split(", ")
# for d in dates:
#     if re.match(pattern, d.strip()):
#         print(f"{d.strip()} → Format de date valide")
#     else:
#         print(f"{d.strip()} → Format de date invalide")
##### autre méthode pour vérifier la validité de la date en utilisant datetime

# import re
# from datetime import datetime
# def verifier_date(date_str):
#     # Vérifier le format avec regex : JJ/MM/AAAA
#     pattern = r"^\d{2}/\d{2}/\d{4}$"
#     if not re.match(pattern, date_str):
#         return False
#     # Vérifier la validité réelle de la date
#     try:
#         datetime.strptime(date_str, "%d/%m/%Y")
#         return True
#     except ValueError:
#         return False
# # Exemple d'utilisation
# dates = ["29/02/2024", "31/04/2023", "15/08/2025", "99/99/9999"]
# for d in dates:
#     print(d, "→", verifier_date(d)) # # DE 1667 à 1960 à il y a 292 lignes de code





