"""# Exercice Python #5 - Bonneteau

## Objectifs

Réaliser un programme permettant de jouer au bonneteau

## Sujet

Réaliser un programme Python qui permet à un utilisateur:
* De voir un ensemble de "gobelets" sans en connaître le contenu
* De choisir un gobelet qui devra être découvert pour en connaître le contenu

Le programme devra: 
* Placer, sous l'un des gobelets (qui seront de base au nombre de 5), une balle. 
* Permettre de chercher sous quel gobelet se trouve la balle
* Mélanger les gobelets (changer la position de la balle) entre chaque tentative de l'utilisateur 

## BONUS 

* Faire en sorte que l'on ait un nombre de tentatives limitées par un compteur de vie
* Réaliser un affichage des gobelets sous la forme d'ASCII art"""
random = __import__('random')
goblets = [False, False, False, False, False]
balle = random.randint(0, 4)
goblets[balle] = True
tentatives = 3
while tentatives > 0:
    print("Voici les gobelets :")
    for i in range(len(goblets)):
        print(f"Gobelet {i + 1}")
    choix = int(input("Choisissez un gobelet (1-5) : ")) - 1
    if goblets[choix]:
        print("Félicitations ! Vous avez trouvé la balle !")
        break
    else:
        print("Dommage, la balle n'est pas là.")
        tentatives -= 1
        if tentatives > 0:
            print(f"Il vous reste {tentatives} tentatives.")
            random.shuffle(goblets)
        else:
            print("Vous avez épuisé toutes vos tentatives. La balle était sous le gobelet " + str(balle + 1) + ".")

