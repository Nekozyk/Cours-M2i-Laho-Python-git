"""
# Exercice Python #1 - Affichage d'un bonjour personnalisé

## Objectifs

Réaliser un jeu du nombre mystère

## Sujet

Réaliser un jeu multijoueur en Python permettant: 
* De choisir un nombre à trouver entre 0 et 100 (compris) pour le joueur UN
* D'entrer un nombre entre 0 et 100 pour le joueur DEUX
    * Le programme devra afficher 'TROP BAS' et redemander le nombre si jamais celui-ci est plus petit que le nombre choisi par l'utilisateur UN 
    * Le programme devra afficher 'TROP HAUT' et redemander le nombre si jamais celui-ci est plus grand que le nombre choisi par l'utilisateur UN 
    * Le programme devra afficher 'FELICITATION' et arrêter de demander des nombres si jamais celui entré est le même que le nombre choisi par l'utilisateur UN

## BONUS

* Générer le nombre à trouver aléatoirement, permettant un mode un joueur
* Ajouter un mode compétitif (le joueur le plus rapide à trouver le nombre gagne, les tour s'alternant entre les deux joueurs)
* Générer deux nombres différents pour chaque joueur dans le mode versus
"""

random = __import__('random')
nombre_mystere = int(random.randint(0, 100))
nombre_de_joueurs = int(input("Entrez le nombre de joueurs (1 ou 2) : "))
chance = []
for i in range(nombre_de_joueurs):
    chance.append(5)

i=0
while True :
    joueur_actuel = i + 1
    print(f"Joueur {joueur_actuel}, vous avez {chance[i]} chances pour trouver le nombre mystère.")    
    nombre_choisi = int(input(f"Joueur {joueur_actuel}, entrez un nombre entre 0 et 100 : "))
    if nombre_choisi < nombre_mystere:
                print("TROP BAS")
                chance[i] -= 1
    elif nombre_choisi > nombre_mystere:
                    print("TROP HAUT")
                    chance[i] -= 1
    else:
                print(f"FELICITATION Joueur {joueur_actuel}, le nombre mystère était bien {nombre_mystere}")
                break
    if chance[i] == 0:
        print(f"Joueur {joueur_actuel}, vous avez épuisé toutes vos chances. Le nombre mystère était {nombre_mystere}.")
        break   

    if joueur_actuel == nombre_de_joueurs:
        i=0
    else:
        i+=1
 
   
        



