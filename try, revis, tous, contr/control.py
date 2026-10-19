
# Exercice 2:  #lasomme et la moyenne
# Début
#     somme ← 0
#     Pour i de 1 à 10 faire
#         Afficher "Entrez le nombre ", i
#         Lire nombre
#         somme ← somme + nombre
#     Fin Pour
#     moyenne ← somme / 10
#     Afficher "La somme est : ", somme
#     Afficher "La moyenne est : ", moyenne
# Fin

# Exercice 1 :
# Début
#     Afficher "Entrez le premier nombre A :"
#     Lire A
#     Afficher "Entrez le deuxième nombre B :"
#     Lire B

#     Si A > B alors
#         Afficher "Le plus grand est : ", A
#     Sinon
#         Afficher "Le plus grand est : ", B
#     Fin Si
# Fin
#######################
##EX 1
# Initialisation de la liste
# etudiants = []
# # Saisie du nombre d'étudiants
# n = int(input("Entrez le nombre d'étudiants : "))

# # Boucle de saisie
# for i in range(n):
#     nom = input(f"Nom de l'étudiant {i+1} : ")
#     note = float(input(f"Note de {nom} : "))
#     etudiants.append((nom, note))

# # Affichage de la liste complète
# print("\nListe des étudiants et leurs notes :")
# print(etudiants)
###########
##EX 2
# # Exemple de liste d'étudiants
# etudiants = [("Taha", 15.5), ("Ali", 18), ("Youssef", 12), ("Sami", 9.5), ("Nora", 17)]

# # 1. Moyenne de la classe
# somme_notes = sum(note for _, note in etudiants)
# moyenne = somme_notes / len(etudiants)
# print("✅ Moyenne de la classe :", round(moyenne, 2))

# # 2. Nombre d'étudiants admis (note ≥ 10)
# admis = [note for _, note in etudiants if note >= 10]
# print("✅ Nombre d'étudiants admis :", len(admis))

# # 3. Étudiant ayant la meilleure note
# meilleur = max(etudiants, key=lambda x: x[1])
# print("✅ Meilleure note :", meilleur[1], "obtenue par", meilleur[0])

# # 4. Notes triées dans l’ordre croissant
# notes_triees = sorted(note for _, note in etudiants)
# print("✅ Notes triées :", notes_triees)

# # 5. Ensemble des noms des étudiants
# noms = set(nom for nom, _ in etudiants)
# print("✅ Noms des étudiants :", noms)
# ####################
# ex 3
# # 1. Création du dictionnaire à partir d'une liste de tuples
# etudiants = [("Taha", 15.5), ("Ali", 18.0), ("Youssef", 12.0)]
# notes = dict(etudiants)

# # 2. Affichage des paires nom / note avec une boucle for
# print("📋 Liste des étudiants :")
# for nom, note in notes.items():
#     print(f"{nom} : {note}")

# # 3. Ajout de l'étudiant "Karim" avec la note 14
# notes["Karim"] = 14.0
# print("\n✅ Étudiant 'Karim' ajouté.")

# # 4. Suppression de l'étudiant "Youssef"
# if "Youssef" in notes:
#     del notes["Youssef"]
#     print("❌ Étudiant 'Youssef' supprimé.")

# # 5. Affichage final du dictionnaire
# print("\n📌 Dictionnaire final :")
# for nom, note in notes.items():
#     print(f"{nom} : {note}")
###################
# # Dictionnaire de départ
# notes = {'Taha': 15.5, 'Ali': 18.0, 'Youssef': 12.0, 'Sami': 9.5, 'Nora': 17.0, 'Karim': 14.0}

# # 1. Fonction pour calculer la moyenne
# def moyenne_notes(d):
#     return sum(d.values()) / len(d)

# # 2. Fonction pour trouver le meilleur étudiant
# def meilleure_note(d):
#     nom = max(d, key=d.get)
#     return nom, d[nom]

# # 3. Fonction pour lister les étudiants admis (note ≥ 10)
# def admis(d):
#     return [nom for nom, note in d.items() if note >= 10]

# # Appels des fonctions et affichage des résultats
# print("✅ Moyenne de la classe :", round(moyenne_notes(notes), 2))

# nom_meilleur, note_meilleur = meilleure_note(notes)
# print(f"🏆 Meilleure note : {note_meilleur} obtenue par {nom_meilleur}")

# print("🎓 Étudiants admis :", admis(notes))

############### import pandas as pd 
# # Création du DataFrame
# import pandas as pd
# data = {
#     'Nom': ['Taha', 'Ali', 'Youssef', 'Sami', 'Nora', 'Karim'],
#     'Note': [15.5, 18.0, 12.0
#              , 9.5, 17.0, 14.0]
# }
# df = pd.DataFrame(data)
# # Affichage du DataFrame
# print("📊 DataFrame des étudiants :")
# print(df) 
# # Calcul de la moyenne des notes
# moyenne = df['Note'].mean()
# print("\n✅ Moyenne des notes :", round(moyenne, 2))
# # Étudiant avec la meilleure note
# meilleur_etudiant = df.loc[df['Note'].idxmax()]
# print("🏆 Meilleure note :", meilleur_etudiant['Note'], "obtenue par", meilleur_etudiant['Nom'])
# # Liste des étudiants admis (note ≥ 10)
# admis = df[df['Note'] >= 10]
# print("🎓 Étudiants admis :"
# , admis['Nom'].tolist())

#############""
# import pandas as pd 
# notes = [12, 15, 14, 10, 13] 
# df_notes = pd.DataFrame(notes, columns=['Note']) 
# df_notes 
# #Moyenne
# moyenne = df_notes['Note'].mean() 
# print("Moyenne :", moyenne)
# #Median
# mediane = df_notes['Note'].median() 
# print("Médiane :", mediane) 
# #Mode
# mode = df_notes['Note'].mode()[0] 
# print("Mode :", mode) 
# # Etendue 
# etendue = df_notes['Note'].max() - df_notes['Note'].min() 
# print("Étendue :", etendue) 
# #Variance et écart-type  
# variance = df_notes['Note'].var() 
# ecart_type = df_notes['Note'].std() 
# print("Variance :", variance) 
# print("Écart-type :", ecart_type) 
# ############"
# import pandas as pd 
# couleurs = ['Rouge', 'Bleu', 'Bleu', 'Vert', 'Rouge'] 
# df_couleurs = pd.DataFrame(couleurs, columns=['Couleur']) 
# df_couleurs 
# #Fréquence absolue et relative 
# freq_abs = df_couleurs['Couleur'].value_counts() 
# freq_rel = df_couleurs['Couleur'].value_counts(normalize=True) * 100 
# print("Fréquence absolue :\n", freq_abs) 
# print("\nFréquence relative (%):\n", freq_rel) 
# #Mode
# mode_couleur = df_couleurs['Couleur'].mode()[0] 
# print("Mode :", mode_couleur) 