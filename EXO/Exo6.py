"""# Exercice Python #6 - Pendu

## Objectifs

Réaliser un programme permettant de jouer au pendu

## Sujet

Réaliser un programme Python qui permet à un utilisateur:
* D'entrer petit à petit des lettres
* Chaque lettre sera ensemble comparée à un mot sélectionné aléatoirement parmi une liste de mots disponible (la sélection se fera par le programme)


A chaque tentative, l'utilisateur pourra voir évoluer l'affichage, qui devra correspondre à quelque chose tel que:

```text
Nombre de vies restantes: XXX
Lettres déjà essayées: [Z, T, X]

Mot à trouver: Z _ _ _ _

Quelle lettre voulez-vous essayer? 
```

## BONUs

* Proposez un mode time-attack où l'utilisateur dispose, en plus d'un nombre de vie limitée, d'un temps limité pour trouver le mot à chercher
* Faire en sorte de demander à trouver plusieurs mots d'affilé du temps que le temps n'est pas encore écoulé"""
import getpass


mot_mystere = getpass.getpass("Entrez le mot mystère (il ne sera pas affiché): ")

chance = 5

while chance > 0:
    lettre = input("Entrez une lettre: ")
    if lettre in mot_mystere:
        print("Bien joué! La lettre est dans le mot.")
    else:
        chance -= 1
        print(f"Raté! Il vous reste {chance} chances.")
    
    # Affichage du mot avec les lettres trouvées
    mot_affiche = ""
    for char in mot_mystere:
        if char in lettre:
            mot_affiche += char + " "
        else:
            mot_affiche += "_ "
    
    print(f"Mot à trouver: {mot_affiche.strip()}")
    
    if "_" not in mot_affiche:
        print("Félicitations! Vous avez trouvé le mot.")
        break
