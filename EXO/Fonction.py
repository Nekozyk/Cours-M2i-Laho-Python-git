
def consulter_notes(notes=[]):
    if not notes :
        print("Aucune note n'a été saisie.")
    else:
        print("Voici l'ensemble des notes :")
        for note in notes:
            print(note)

def plus_petite_note(notes):
    if not notes:
        print("Aucune note n'a été saisie.")
    else:
        print(f"La plus petite note est : {min(notes)}")

def plus_grande_note(notes):
    if not notes:
        print("Aucune note n'a été saisie.")
    else:
        print(f"La plus grande note est : {max(notes)}")

def moyenne_notes(notes):
    if not notes:
        print("Aucune note n'a été saisie.")
    else:
        moyenne = sum(notes) / len(notes)
        print(f"La moyenne des notes est : {moyenne:.2f}")

def consulter_notes_par_matiere(notes_matiere):
    if not notes_matiere:
        print("Aucune note n'a été saisie.")
    else:
        taille_separateur = 10
        #trouver la taille du séparateur en fonction de la plus longue matière
        for matiere in notes_matiere.keys():
            if len(matiere) > taille_separateur:
                taille_separateur = len(matiere)

        print(f"{'Matière':<{taille_separateur}}|{'Notes':<{taille_separateur}}")
        print("-"*taille_separateur+"†"+"-"*taille_separateur)
        
        for matiere, notes in notes_matiere.items():
            print(f"{matiere:<{taille_separateur}}|{', '.join(map(str, notes)):<{taille_separateur}}")
            print("-"*taille_separateur+"†"+"-"*taille_separateur)

def plus_petite_note_par_matiere(notes_matiere):
    if not notes_matiere:
        print("Aucune note n'a été saisie.")
    else:
        matiere_petite_note = ""
        petite_note = float(0.0)
        for matiere, notes in notes_matiere.items():
            if min(notes) < petite_note or petite_note == 0.0:
                petite_note = min(notes)
                matiere_petite_note = matiere

        print(f"La plus petite note pour la matière {matiere_petite_note} est : {petite_note}")

def plus_grande_note_par_matiere(notes_matiere):
    if not notes_matiere:
        print("Aucune note n'a été saisie.")
    else:
        matiere_grande_note = ""
        grande_note = float(0.0)
        for matiere, notes in notes_matiere.items():
            if max(notes) > grande_note:
                grande_note = max(notes)
                matiere_grande_note = matiere
        print(f"La plus grande note pour la matière {matiere_grande_note} est : {grande_note}")

def moyenne_notes_par_matiere(notes_matiere):
    if not notes_matiere:
        print("Aucune note n'a été saisie.")
    else:
        for matiere, notes in notes_matiere.items():
            moyenne = sum(notes) / len(notes)
    print(f"La moyenne des notes pour toutes les matières est : {moyenne:.2f}")