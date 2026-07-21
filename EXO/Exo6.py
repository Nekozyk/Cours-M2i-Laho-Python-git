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
mot_affiche = "_" * len(mot_mystere)
chance = 7
lettre_deja_test =set()
while chance > 0:
      print("Mot à trouver:", mot_affiche)
      lettre = input("Entrez une lettre: ")
      lettre_deja_test.add(lettre)
      if lettre in mot_mystere:
        print("Bien joué! La lettre est dans le mot.")
      else:
        chance -= 1
        print(f"Raté! Il vous reste {chance} chances.")
    
    # Affichage du mot avec les lettres trouvées

      for i in range(len(mot_mystere)):
        if mot_mystere[i] == lettre:
            mot_affiche = mot_affiche[:i] + lettre + mot_affiche[i+1:]
  
      print("lettre testé " ,list(lettre_deja_test))
      if mot_mystere == mot_affiche:
        print("Félicitations! Vous avez trouvé le mot.")
        break

print("Le mot mystère était:", mot_mystere)
