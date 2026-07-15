"""# Exercice Python #4 - Carnet de notes

## Objectifs

Réaliser un programme permettant d'entrer un ensemble de notes pour nos élèves

## Sujet

Réaliser un programme Python qui permet à un utilisateur:
* D'entrer un ensemble de notes
* De connaître la plus grande note
* De connaître la plus petite note
* De connaître la moyenne des notes

Pour cela, un menu sera disponible pour l'utilisateur, sous la forme:

```text
=== PROGRAMME NOTES ===
1. Entrer une nouvelle note
2. Consulter l'ensemble des notes
3. Connaître la plus petite note
4. Connaître la plus grande note
5. Connaître la moyenne des notes
0. Quitter
```

## BONUS

* Faire en sorte de pouvoir entrer les notes par matière. Permettre de connaître les plus grandes, plus petites, la moyenne des notes par matière également.
* Faire en sorte, pour chaque note, de stocker également le nom, le prénom, la classe, la date, l'heure de l'examen et la matière concernée
* Permettre, lors de la visualisation des notes, d'avoir un affichage sous forme de tableau au format fixe
"""
import Fonction

notes = []
notes_matiere = {}

while True:
    print("""
          === PROGRAMME NOTES ===  
            1. Entrer une nouvelle note
            2. Consulter l'ensemble des notes
            3. Connaître la plus petite note
            4. Connaître la plus grande note
            5. Connaître la moyenne des notes
            6. Entrer une nouvelle note par matière
            7. Consulter l'ensemble des notes par matière
            8. Connaître la plus petite note par matière
            9. Connaître la plus grande note par matière
            10. Connaître la moyenne des notes par matière
            0. Quitter""")

    choix = input("Votre choix : ")

    if choix == "1":
        try:
            note = float(input("Entrez une nouvelle note : "))
            notes.append(note)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    elif choix == "2":
        Fonction.consulter_notes(notes)
    elif choix == "3":
        Fonction.plus_petite_note(notes)
    elif choix == "4":
        Fonction.plus_grande_note(notes)
    elif choix == "5":
        Fonction.moyenne_notes(notes)
    elif choix == "6":
        matiere = input("Entrez le nom de la matière : ")
        try:
            note = float(input("Entrez une nouvelle note : "))
            if matiere not in notes_matiere:
                notes_matiere[matiere] = []
            notes_matiere[matiere].append(note)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    elif choix == "7":
        Fonction.consulter_notes_par_matiere(notes_matiere)
    elif choix == "8":
        Fonction.plus_petite_note_par_matiere(notes_matiere)
    elif choix == "9":
        Fonction.plus_grande_note_par_matiere(notes_matiere)
    elif choix == "10":
        Fonction.moyenne_notes_par_matiere(notes_matiere)
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
