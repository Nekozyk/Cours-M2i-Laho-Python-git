"""# Exercice Python #2 - Commande de nourriture

## Objectifs

Créer un programme de commande de nourriture

## Sujet

Réaliser un programme en Python permettant à l'utilisateur: 
* De choisir un ensemble de boissons / nourriture parmi une liste fixe
* De voir le prix de chacun des articles
* De choisir un article et de se voir demandé le prix à payer

## BONUS

* Ajouter une somme d'argent totale que l'utilisateur peut consommer. Il pourra ainsi apprécier, pour chaque achat, la réduction en temps réel de son porte-monnai
* Faire en sorte de faire une commande complète avant de valider l'achat. Dans ce cas là, l'utilisateur pourra voir en temps réel la somme de sa commande évoluer avant de confirmer l'achat
"""
argent_client = 50.0
facture = 0.0

while True:
    print("Voici la liste des articles disponibles :")
    print("1. Boisson - 5€")
    print("2. Nourriture - 10€")
    print("3. Dessert - 7€")
    print("4. Quitter")
    choix = input("Entrez le numéro de l'article que vous souhaitez acheter : ")
    
    match choix:
        case "1":   
            article = "Boisson"
            facture += 5.0
        case "2":   
            article = "Nourriture"
            facture += 10.0
        case "3":   
            article = "Dessert"
            facture += 7.0
        case "4":
            argent_client -= facture
            print(f"Merci d'avoir utilisé notre service de commande de nourriture ! votre facture est de {facture}€ et il vous reste {argent_client}€.")
            break
        case _:  
            print("Choix invalide.")
            continue
   
    if argent_client<facture:
             print(f"Vous n'avez pas assez d'argent pour acheter {article}.La facture est de {facture}€. Il vous reste {argent_client}€.")
             break
    

