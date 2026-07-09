# Exercice Python #1 - Affichage d'un bonjour personnalisé

## Objectifs Appréhender la manipulation des entrées et sorties via une chaine de caractère

""" Sujet

Réaliser un programme en Python permettant à l'utilisateur: 
* D'entrer son NOM
* D'entrer son PRENOM
* D'entrer son AGE 

Une fois fait, le programme offrira un message personnalisé tel que:

```text
Bonjour John DUPONT, vous avez 24 ans!
```

## BONUS

Faire en sorte de demander à entrer la date du jour (ou de la récupérer directement) et la date de naissance à la place

"""
from datetime import datetime
import sys


nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")    
age = int(input("Entrez votre âge : "))

print(f"Bonjour {prenom} {nom}, vous avez {age} ans!")
print("nous sommes le " + datetime.now().strftime("%d/%m/%Y"))
date_naissance = input("Entrez votre date de naissance (jj/mm/aaaa) : ")
age_calcul = datetime.now().year - datetime.strptime(date_naissance, "%d/%m/%Y").year
if age_calcul != age:   
    print(f"Attention, l'âge calculé à partir de votre date de naissance est {age_calcul}, ce qui ne correspond pas à l'âge que vous avez entré ({age}).")
else:
    print(f"Votre âge est correct, vous avez {age_calcul} ans.")
    if datetime.now().month == datetime.strptime(date_naissance, "%d/%m/%Y").month and datetime.now().day == datetime.strptime(date_naissance, "%d/%m/%Y").day:
        print("Joyeux anniversaire !")     
    elif datetime.now().month != datetime.strptime(date_naissance, "%d/%m/%Y").month and datetime.now().day != datetime.strptime(date_naissance, "%d/%m/%Y").day:
        print("Ce n'est pas votre anniversaire aujourd'hui.")