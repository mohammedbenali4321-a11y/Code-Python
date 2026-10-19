# N = int(input("Entrez un entier N : "))
# somme = N * (N + 1) // 2
# print("La somme des entiers de 1 à", N, "est :", somme)
####################################################
# n = int(input("Entrez un entier N :"))
# for i in range(1,12):
#    print(f"{n} * (i) = {n*i}")
####################################################
# n = 10
# for i in range( 1, n+1):
#  print('*' * i)
##################################################
# l = [13,17,2,5,9,47,17,20]
# vide =[]
# vide1 = list(range(0,1001,2))
# print(vide1)
##################################################
# name = 'abderrahman'
# name_changer = name.replace("abderrahman","abderrah0an")  
# print(name_changer)
#################################################
def saluer(nom= 'itoo' ) :
 saluer()
def add(a,b):
    somme = a + b
    return somme
d = lambda a,b : a+b
print(d(7,9))
########################################
# number = (12, 24, 'abdo', 0)
# a, b, c, d = number
# print(number)
############################################
# # Définition de la fonction pour supprimer les nombres impairs
# n = (-1, 0, 30, 19, 7, 40, 4)

# def supprimer(n):
#     m = []
#     for i in n:
#         if i % 2 == 0:  # Correction ici : == au lieu de =
#             m.append(i)
#     return tuple(m)

# # Appel de la fonction et affichage du résultat
# print(supprimer(n))
############################################
# ensemble = {1,3,5,7,8,10,18,24}
# print("la taille de l'ensemble",len(ensemble))
# print("le max de l'ensembe",max(ensemble))
# print("le min de l'ensembe",min(ensemble))
# print("le som de l'ensembe",sum(ensemble)
#####################################
# etudiant = {
#    "nom" : "Itooo" ,
#    "age" : 20  , 
#    "poids" : 60}
# etudiant.pop("nom")
# etudiant.pop("age")
# print(etudiant)
# etudiant ["age"] = "20"
# etudiant ["name"] = "Itooo"
# etudiant ["name"] = "moha"
# etudiant ["longueur"] = "1,80"
# print (etudiant)
###############################
# ##اختر أحد الطريقتين فقط:
# ##الطريقة 1: باستخدام الإسناد المباشر
# ##الطريقة 2: باستخدام 
# stock = {"pomme": 50, "banane": 30, "orange": 20}
# #1stock["Ananas"] = 40
# #2 stock.update({"Ananas": 40})
# print(stock)
##############################
# melange = [('anas' , 20) , ('yassine' , 18) ,('taha' , 24) ]
## test = sorted(melange, key=lambda ih: ih[1])
#  test = sorted(melange , key = lambda ih:ih[0], reverse=False )
# print(test)
#########################
# numbers = [1, 4, 5]

# def impaire(x):
#     return x % 2 != 0

# test = list(filter(impaire, numbers))
# print(test)
##########################
# def carre(x): 
#    return x**2
# def cube(x):
#     return x**3
# def puissance4(x):
#     return x**4
# def puissance5(x):
#     return x**5
# def puissance9(x):
#     return x**9
# x=int(input("Entrez une nombre entier"))
# print(f"{x} a la puissance 2 est egale {carre(x)}")
# print(f"{x} a la puissance 3 est egale {cube(x)}")
# print(f"{x} a la puissance 4 est egale {puissance4(x)}")
# print(f"{x} a la puissance 5 est egale {puissance5(x)}")
# print(f"{x} a la puissance 9 est egale {puissance9(x)}")
#########################""
# def doubler(x):
#     return x * 2

# résultat = doubler(4)
# print(résultat)  # يعرض: 8
#################################
# def puissance(x, y):
#     return x ** y

# nombre = int(input("Entrez un entier : "))
# résultat = puissance(nombre, 2)
# print("Le carré est :", résultat)
################################
##استيراد مكتبة os
##يتحقق هل المجلد "dossier" موجود بالفعل
##ينشئ مجلدًا جديدًا
##عرض المسار الحالي الذي يعمل فيه البرنامج
# import os
# os.path.exists("piw")
# os.mkdir("piw") 
# print(os.getcwd()) 
#####################
##استيراد معلومات النظام
# import sys 
# print("Version de Python :", sys.version) 
########################
##استيراد أدوات التحكم في الوقت
# import time 
# print("Heure actuelle :", time.ctime()) 
# time.sleep(2)   # pause de 2 secondes 
###############

# print("Reprise du programme")
# import math, random, datetime 
# r = random.randint(1, 10) 
# aire = math.pi * r**2 
# print("Rayon :", r) 
# print("Aire du cercle :", round(aire, 2)) 
# print("Calcul effectué le :", datetime.date.today())
################################
# "لعبة التخمين التفاعلية"
# import random
# X= random.randint(1, 100)
# while True:
#     devinette = int(input("Entrez le entier entre (1, 100)") )
#     if devinette == X :
#         print("bon, tu as gagné")
#         break
#     elif X < devinette :
#          print("Trop grand !")
#     elif X > devinette :
#          print("trop petit!")
#################################
# import random
# # 🎲 Générer un nombre aléatoire entre 1 et 100
# X = random.randint(1, 100)
# # 🔢 Initialiser le compteur de tentatives
# tentatives = 0
# max_tentatives = 8
# print("🎮 Bienvenue dans le jeu de devinette !")
# print(f"🔢 Devinez le nombre entre 1 et 100 (maximum {max_tentatives} tentatives)")
# # 🔁 Boucle de jeu
# while tentatives < max_tentatives:
#     try:
#         devinette = int(input("👉 Entrez votre nombre : "))
#         tentatives += 1
#         if devinette == X:
#             print(f"🎉 Bravo ! Vous avez gagné en {tentatives} tentative(s).")
#             break
#         elif devinette > X:
#             print("📉 Trop grand !")
#         else:
#             print("📈 Trop petit !")
#         # 💡 Afficher le nombre de tentatives restantes
#         print(f"⏳ Tentatives restantes : {max_tentatives - tentatives}")
#     except ValueError:
#         print("⚠️ Veuillez entrer un nombre entier valide.")
# # ❌ Si le joueur dépasse le nombre de tentatives
# if tentatives == max_tentatives and devinette != X:
#     print(f"😢 Vous avez épuisé vos {max_tentatives} tentatives. Le nombre était {X}.")
############################################
# import tkinter as tk
# from tkinter import messagebox
# import random

# # 🎲 توليد رقم عشوائي
# nombre_secret = random.randint(1, 100)
# tentatives = 0
# max_tentatives = 10

# # 🖼️ إعداد النافذة
# fenetre = tk.Tk()
# fenetre.title("Jeu de Devinette")
# fenetre.geometry("300x200")

# # 📝 وظيفة التحقق
# def verifier():
#     global tentatives
#     try:
#         guess = int(entree.get())
#         tentatives += 1

#         if guess == nombre_secret:
#             messagebox.showinfo("Bravo !", f" vous avez trouvé le nombre en {tentatives} tentative(s) .")
#             fenetre.destroy()
#         elif tentatives >= max_tentatives:
#             messagebox.showerror("Échec", f" Vous avez épuisé vos tentatives. Le nombre était {nombre_secret}.")
#             fenetre.destroy()
#         elif guess > nombre_secret:
#             resultat.config(text=" Trop grand !")
#         else:
#             resultat.config(text=" Trop petit !")

#         compteur.config(text=f"Tentatives restantes : {max_tentatives - tentatives}")

#     except ValueError:
#         messagebox.showwarning("Erreur", "Veuillez entrer un nombre entier.")

# # 🧩 عناصر الواجهة
# label = tk.Label(fenetre, text="Devinez le nombre (1 à 100) :")
# label.pack(pady=10)

# entree = tk.Entry(fenetre)
# entree.pack()

# bouton = tk.Button(fenetre, text="Vérifier", command=verifier)
# bouton.pack(pady=5)

# resultat = tk.Label(fenetre, text="")
# resultat.pack()

# compteur = tk.Label(fenetre, text=f"Tentatives restantes : {max_tentatives}")
# compteur.pack(pady=5)

# # ▶️ تشغيل الواجهة
# fenetre.mainloop()
###############################

# import random
# class JeuNombreMystere:
#     def __init__(self, max_tentatives=None):
#         self.__max_tentatives = max_tentatives
#         self.reinitialiser()
#     def reinitialiser(self):
#         self.__nombre_secret = random.randint(1, 100)
#         self.__tentatives = 0
#         self.__gagne = False
#     def deviner(self, nombre):
#         if self.__gagne:
#             return " ta as déjà gagnée ! rejouez en cours."
#         self.__tentatives += 1
#         if nombre > self.__nombre_secret:
#             return "Trop grand !"
#         elif nombre < self.__nombre_secret:
#             return "Trop petit !"
#         else:
#             self.__gagne = True
#             return f"Bravoooooo...O. Trouver en {self.__tentatives} essais !"
#     def afficher_indice(self):
#         if self.__tentatives > 10:
#             if self.__nombre_secret % 2 == 0:
#                 return "Indice : le nombre est pair."
#             else:
#                 return "indicee : le nombre est impair."
#         return " pas d'indice disponible ."
#     def __str__(self):
#         if self.__gagne:
#             return f" gagnée en {self.__tentatives} essais. Le nombre secret était {self.__nombre_secret}."
#         else:
#             return f" en cours : {self.__tentatives} tentatives effectues."
# if __name__ == "__main__":
#     jeu = JeuNombreMystere()
#     print("bienvenue dans le jeu du nombre mystère !")
#     print("Welcome to the mystery number game!")
#     while True:
#         try:
#             proposition = int(input("devinez le nombre (entre 1 et 100) : "))
#             resultat = jeu.deviner(proposition)
#             print(resultat)
#             if "Bravooooooooooo" in resultat:
#                 print(jeu)
#                 rejouer = input(" voulez-vous rejouer ? (o/n) : ").lower()
#                 if rejouer == "o":
#                     jeu.reinitialiser()
#                 else:
#                     print(" merci d'avoir joue !. Au revoir")
#                     break
#             if not jeu.__str__().startswith(" tu as gagnée"):
#                 print(jeu.afficher_indice())
#         except ValueError:
#             print("il faut  entrer un nombre entier valide.")


##################################################3
# import math
# print(math.sqrt(81) )
#######################################################
# import math
# math.degrees
# x = 5.7
# print(math.sqrt(81) )
# print("L’arrondi supérieur  et inférieur de 5.7 : ", math.ceil(x) ,"\n" ,math.floor(x))
# print("le sinus de 90° : " , math.sin(x), math.degrees )
#################################################33

# import datetime 
# maintenant = datetime.datetime.now() 
# print("Date et heure actuelles :", maintenant) 
#########################################33
# f = ope
# n("té.txt", "w") 
# f.write("Ceci est la première ligne.\n") 
# lignes = ["Ligne 1\n\n", "Ligne 2\n", "Ligne 3\n"] 
# f = open("multi.txt", "w") 
# f.writelines(lignes) 
# f.close()
# # comment routerner deux foix a la ligne  \n : 
#####################################333
# f = open("TONTO.txt", "w") 
# f.write(" Bonjour\n")
# f.write("Je découvre la gestion des fichiers en Python\n")
# f.close()
####################################################
##erreur 
# f = open("maniche.txt", "r+") 
# for ligne in f: 
#  print(ligne.strip())
#  f.close()
## corriger 
# try:
#     f = open("maniche.txt", "r", encoding="utf-8")
#     for ligne in f:
#         print(ligne.strip())
#     f.close()
# except FileNotFoundError:
#     print("❌ Le fichier 'maniche.txt' est introuvable.")
# except Exception as e:
#     print("⚠️ Une erreur est survenue :", e)
###################################""""
# f = open("exemple.txt", "a") 
# f.write(" C’est facile d’écrire dans un fichier hhhhh !\n") 
# f.close()
###############################
# # Exercice 1 : Création du dictionnaire produit
# import json
# produit = {
#     "nom": "Ordinateur",
#     "prix": 7500,   
#     "stock": 12}
# # # #Sauvegarde dans le fichier produit.json
# with open("produit.json", "w", encoding="utf-8") as fichier:
#     # json.dump(produit, fichier, ensure_ascii=False, indent=4)
#     json.dump(produit, fichier, indent=4)
# # # Exercice 2 : Lecture du fichier produit.json
# import json
# with open("prodouit.json", "r", encoding="utf-8") as f:
#     produit = json.load(f)
############################  dictionaire des données
# produit = {
#     "nom": "Ordinateur",
#     "prix": 7500,
#     "stock": 12}
# ## Affichage des informations
# print("Produit :", produit["nom"])
# print("Prix :", produit["prix"], "DH")
# print("Stock disponible :", produit["stock"])
####################################""
##une chance
# print("Quelle fonction donne la longueur d'une liste ?")
# print("A) lenght()")
# print("B) len()")
# print("C) size()")

# reponse = input("Choisir A, B ou C : ").strip().upper()
# if reponse == "B":
#     print("CORRECT ")
# else:
#     print("INCORRECT ")
###########""
##deux chance
# print("Quelle fonction donne la longueur d'une liste ?")
# print("A) lenght()")
# print("B) len()")
# print("C) size()")
# reponse = input("Choisir A, B ou C : ").strip().upper()
# if reponse == "B":
#     print(" CORRECT !")
# else:
#     print(" INCORRECT. Essaie encore une fois.")
#     reponse2 = input("Deuxième chance - Choisir A, B ou C : ").strip().upper()
#     if reponse2 == "B":
#         print(" Bien joué ! C'était la bonne réponse.")
#     else:
#         print(" Mauvaise réponse. La bonne fonction est len().")
###########
##tois chance
# print("Quelle fonction donne la longueur d'une liste ?")
# print("A) lenght()")
# print("B) len()")
# print("C) size()")
# tentatives = 0
# bonne_reponse = "B"
# while tentatives < 3:
#     reponse = input(f"Choisir A, B ou C (tentative {tentatives + 1}/3) : ").strip().upper()
#     if reponse == bonne_reponse:
#         print("✅ CORRECT !")
#         break
#     else:
#         tentatives += 1
#         if tentatives < 3:
#             print(" INCORRECT. Essaie encore.")
#         else:
#             print(" Mauvaise réponse. La bonne fonction est len().")
###
##TROIS CHANCE D'une autre manieré
# bonne_reponse = "B"
# print("Quelle fonction donne la longueur d'une liste ?")
# print("A) lenght()")
# print("B) len()")
# print("C) size()")
# for tentative in range(1, 4):
#     reponse = input(f"Tentative {tentative}/3 - Choisir A, B ou C : ").strip().upper()  
#     if reponse == bonne_reponse:
#         print(" CORRECT !")
#         break
#     else:
#         if tentative < 3:
#             print(" INCORRECT. Essaie encore.")
#         else:
#             print(" Mauvaise réponse. La bonne fonction est len().")