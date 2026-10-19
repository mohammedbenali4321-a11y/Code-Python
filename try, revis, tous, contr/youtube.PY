# # # character_name= "mourad"
# # # age= "66"
# # # is_male = False
# # # print('there was a boy called ' + character_name + " hecham" )
# # # print("he was " + age + ' years old')
# # # character_name= " itoo "
# # # age ="20"
# # # print('he liked his name ' +  character_name )
# # # print("but wase'nt happy about being " +age)

# text = "MOHaMED BeN ali"
# last_name = "ben ali"
# first_name = "mohamed"
# print(text.replace("ED","ed"))
# print(text.index("BeN"))
# print(last_name[0],first_name[2])
# print(text[6])
# print (len(text))
# print(text.lower().islower()) # transfere la phrase au miniscule et vue si la phrase est en miniscule
# # print(text.islower())
# # print(text.isupper())
# print(text.upper().isupper())  # le contraire de islower
# # print(text.isupper())
# # print(text.islower())
# print(text+"is cool because its the best coding school")  # add somthing to the first sentence
# print("mohamed \nben \nali") #comme to newlie

##############
# tkherbi9

# import json
# # 📌 Exceptions personnalisées
# class EtudiantExisteException(Exception):
#     pass
# class EtudiantIntrouvableException(Exception):
#     pass
# # 👤 Classe Etudiant
# class Etudiant:
#     def __init__(self, nom, notes=None):
#         self.__nom = nom
#         self.__notes = notes if notes else []
#     def get_nom(self):
#         return self.__nom
#     def get_notes(self):
#         return self.__notes
#     def set_notes(self, nouvelles_notes):
#         self.__notes = nouvelles_notes
#     def ajouter_note(self, note):
#         self.__notes.append(note)
#     def modifier_notes(self, nouvelles_notes):
#         self.__notes = nouvelles_notes
#     def moyenne(self):
#         return sum(self.__notes) / len(self.__notes) if self.__notes else 0
#     def __str__(self):
#         return f"Étudiant: {self.__nom}, Notes: {self.__notes}, Moyenne: {self.moyenne():.2f}"
#     def to_dict(self):
#         return {"nom": self.__nom, "notes": self.__notes}
#     @staticmethod
#     def from_dict(data):
#         return Etudiant(data["nom"], data["notes"])
# # 🗂️ Classe GestionnaireEtudiants
# class GestionnaireEtudiants:
#     def __init__(self):
#         self.__etudiants = {}
#     def ajouter_etudiant(self, etudiant):
#         nom = etudiant.get_nom()
#         if nom in self.__etudiants:
#             raise EtudiantExisteException(f"L'étudiant '{nom}' existe déjà.")
#         self.__etudiants[nom] = etudiant
#     def supprimer_etudiant(self, nom):
#         if nom not in self.__etudiants:
#             raise EtudiantIntrouvableException(f"L'étudiant '{nom}' est introuvable.")
#         del self.__etudiants[nom]
#     def modifier_notes(self, nom, nouvelles_notes):
#         if nom not in self.__etudiants:
#             raise EtudiantIntrouvableException(f"L'étudiant '{nom}' est introuvable.")
#         self.__etudiants[nom].modifier_notes(nouvelles_notes)
#     def afficher_moyennes(self):
#         for etudiant in self.__etudiants.values():
#             print(etudiant)
#     def moyenne_generale(self):
#         if not self.__etudiants:
#             return 0
#         total = sum(e.moyenne() for e in self.__etudiants.values())
#         return total / len(self.__etudiants)
#     def meilleur_etudiant(self):
#         if not self.__etudiants:
#             return None
#         return max(self.__etudiants.values(), key=lambda e: e.moyenne())
#     def classement(self):
#         return sorted(self.__etudiants.values(), key=lambda e: e.moyenne(), reverse=True)
#     def sauvegarder(self, fichier):
#         with open(fichier, "w", encoding="utf-8") as f:
#             data = [e.to_dict() for e in self.__etudiants.values()]
#             json.dump(data, f, ensure_ascii=False, indent=2)
#     def charger(self, fichier):
#         try:
#             with open(fichier, "r", encoding="utf-8") as f:
#                 data = json.load(f)
#                 for e in data:
#                     self.ajouter_etudiant(Etudiant.from_dict(e))
#         except FileNotFoundError:
#             pass
# def menu():
#     gestionnaire = GestionnaireEtudiants()
#     gestionnaire.charger("etudiants.json")
#     while True:
#         print("\n ---MENU_génèrale---")
#         print("1. Ajouter un étudiant")
#         print("2. Supprimer un étudiant")
#         print("3. Modifier les notes d’un étudiant")
#         print("4. Afficher les moyennes")
#         print("5. Moyenne générale de la classe")
#         print("6. Meilleur étudiant")
#         print("7. Classement des étudiants")
#         print("8. Sauvegarder et quitter")
#         choix = input("Choix : ")
#         try:
#             if choix == "1":
#                 nom = input("Nom de l’étudiant : ")
#                 notes = list(map(float, input("Notes séparées par des espaces : ").split()))
#                 gestionnaire.ajouter_etudiant(Etudiant(nom, notes))
#                 print(" Étudiant ajouté.")
#             elif choix == "2":
#                 nom = input("Nom de l’étudiant à supprimer : ")
#                 gestionnaire.supprimer_etudiant(nom)
#                 print(" Étudiant supprimé.")
#             elif choix == "3":
#                 nom = input(" Nom de l’étudiant : ")
#                 notes = list(map(float, input("Nouvelles notes : ").split()))
#                 gestionnaire.modifier_notes(nom, notes)
#                 print(" Notes modifiées.")
#             elif choix == "4":
#                 gestionnaire.afficher_moyennes()
#             elif choix == "5":
#                 print(f" moyenne générale : {gestionnaire.moyenne_generale():.2f}")
#             elif choix == "6":
#                 meilleur = gestionnaire.meilleur_etudiant()
#                 if meilleur:
#                     print(f" Meilleur étudiant : {meilleur}")
#                 else:
#                     print("aaucun étudiant enregistré.")
#             elif choix == "7":
#                 print(" classement des étudiants :")
#                 for i, etu in enumerate(gestionnaire.classement(), 1):
#                     print(f"{i}. {etu.get_nom()} - Moyenne : {etu.moyenne():.2f}")
#             elif choix == "8":
#                 gestionnaire.sauvegarder("etudiants.json")
#                 print("données sauvegardées. À bientôt !")
#                 break
#             else:
#                 print("choix invalide.")
#         except (EtudiantExisteException, EtudiantIntrouvableException, ValueError) as e:
#             print(f"Errrrreur : {e}")
# if __name__ == "__main__":
#     menu()

#  def moyenne_generale(self):
#         som = 0 
#         for etudiant in self.__etudiants.values():
#             som+=etudiant
#         print(som/len(self.__etudiants))  


#################
# # calculer la corilationde pearson entre deux listes
# heur = [2, 5, 12,15]
# note= [1, 0, 8, 10]
# m1= sum (heur)/ len (heur)
# m2= sum (note)/ len (note)
# s1=0
# s2=0        
# s3=0  
# for i in range (len(note)):
#     s1+= (note[i]-m1)*(heur[i]-m2)
#     s2+= (note[i]-m2)**2
#     s3+= (heur[i]-m1)**2
#     numererator= s1             
#     denominator= (s2*s3)**0.5
# resultat= numererator/denominator
# print("le coefficient de correlation de pearson est :", resultat)     

# coefficient_correlation = resultat
# if coefficient_correlation > 0: 
#     print("Il y a une corrélation positive entre les deux variables.")
# elif coefficient_correlation < 0:
#     print("Il y a une corrélation négative entre les deux variables.")
# intrepretation = abs(coefficient_correlation)
# if intrepretation >= 0.7:
#     print("La corrélation est forte.")  
# elif intrepretation >= 0.4:
#     print("La corrélation est modérée.")    
# elif intrepretation >= 0.1:
#     print("La corrélation est faible.")
# else:
#     print("Il n'y a pas de corrélation.")

# def correlation_pearson(x, y):
#     n = len(x)
#     sum_x = sum(x)
#     sum_y = sum(y)
#     sum_x2 = sum(i**2 for i in x)
#     sum_y2 = sum(i**2 for i in y)
#     sum_xy = sum(x[i] * y[i] for i in range(n))
#     numerator = n * sum_xy - sum_x * sum_y
#     denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5
#     if denominator == 0:
#         return 0
#     return numerator / denominator      
# resultat = correlation_pearson(heur, note)
# print("Le coefficient de corrélation de Pearson est :", resultat)
############
# Parfait Mohamed ✨, tu veux voir **la manière de calculer la corrélation** pas seulement le résultat. Allons étape par étape avec la formule du coefficient de corrélation de Pearson :
# ---
# ## 📐 Formule
# \[
# r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \cdot \sum (y_i - \bar{y})^2}}
# \]

# - \(x_i\) = heures d’étude  
# - \(y_i\) = notes  
# - \(\bar{x}\) = moyenne des heures  
# - \(\bar{y}\) = moyenne des notes  

# ---

# ## 🔎 Étapes de calcul

# 1. **Moyennes :**
#    - \(\bar{x} = \frac{0+1+8+10}{4} = 4.75\)  
#    - \(\bar{y} = \frac{2+5+12+15}{4} = 8.5\)

# 2. **Écarts à la moyenne :**
#    - Heures : \([-4.75, -3.75, 3.25, 5.25]\)  
#    - Notes : \([-6.5, -3.5, 3.5, 6.5]\)

# 3. **Produits croisés :**
#    - \((-4.75 \cdot -6.5) = 30.875\)  
#    - \((-3.75 \cdot -3.5) = 13.125\)  
#    - \((3.25 \cdot 3.5) = 11.375\)  
#    - \((5.25 \cdot 6.5) = 34.125\)  
#    - **Somme = 89.5**

# 4. **Carrés des écarts :**
#    - Heures² : \(22.56 + 14.06 + 10.56 + 27.56 = 74.75\)  
#    - Notes² : \(42.25 + 12.25 + 12.25 + 42.25 = 109\)

# 5. **Corrélation :**
#    \[
#    r = \frac{89.5}{\sqrt{74.75 \cdot 109}} \approx 0.9915
#    \]



# ------------
# probabalite de evenement  D = 0.7
# commment calculer la probabilité de l'événement complémentaire D ? 
# La probabilité de l'événement complémentaire D est calculée en utilisant la formule suivante :
# P(D') = 1 - P(D)
# Dans ce cas, si P(D) = 0.7, alors :
# P(D') = 1 - 0.7 = 0.3 
# ______________________________________________________________________________________________________________________________
# exercice 1:
# 2:
# P_D = 18/40
# print(" la probabilite de evenement  D est :", P_D)
# P_I = 15/40
# print(" lla probabilite de evenement I est :", P_I)
# P_D_inter_I = 7/40
# print(" la probabilite de evenement D inter I est :", P_D_inter_I)
# P_D_union_I = P_D + P_I - P_D_inter_I
# print(" la probabilite de evenement D union I est :", P_D_union_I)
# # 3:
# P_no_D_no_I = 1 - P_D_union_I
# print(" la probabilite d'un etudiant ne suivent pas aucune option est :", P_no_D_no_I)
# # 4:
# P_D_union_I_verifie = P_D + P_I - P_D_inter_I
# print(" verification la coherence des resultats:", P_D_union_I_verifie)
 
# exercice 2:
# 2:
TOTAL = 40
d = 18
i = 15
di = 7
P_D = d / TOTAL
print(" la probabilite de evenement  D est :", P_D)
P_I= i / TOTAL
print(" la probabilite de evenement  I est :", P_I)
P_D_inter_I = di / TOTAL    
print(" la probabilite de evenement D inter I est :", P_D_inter_I)
P_D_union_I = P_D + P_I - P_D_inter_I
print(" la probabilite de evenement D union I est :", P_D_union_I)
# autre methode
P_A = 3/6
print(" la probabilite de evenement  A est :", P_A)
P_B = 3/6
print(" la probabilite de evenement  B est :", P_B)
# pour A inter B
P_A_inter_B = P_A * P_B
print(" la probabilite de evenement A inter B est :", P_A_inter_B)
# 3: 
P_A_inter_B= P_A * P_B
print(" la probabilite de evenement A inter B est :", P_A_inter_B)


