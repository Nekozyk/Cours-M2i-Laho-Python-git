def Action_Joueur_combat(ennemi):
    print(f"""Vous parcourez la galerie, vous rencontrez un {ennemi} que faite vous ?
          
            1.Attaquer
            2.Fuir comme un lache
          """)
    choix = int(input("Votre choix : "))
    return choix

def Action_forge(personnage):
    print("Vous entrez chez le forgeron qui vous propose d'améliorer votre arme :")

def Action_amurie(personnage):
    print("Vous entrez chez l'armurier qui vous propose d'améliorer votre armure :")    

def Action_Dispensaire(personnage):
    print("Vous entrez chez l'apoticaire qui vous propose de vous soigner :")

def Action_Camp(personnage):
    print("Vous entrez chez l'instructeur qui vous propose d'améliorer votre compétence martial :")
    


def Action_Joueur_village(personnage):
    print(f"""Vous entrez au village, plusieurs échoppe se présente à vous, où allez vous ?
            
          1.Forgeron (amélioration d'armes)
          2.Armurie (amélioration de l'armure)
          3.Dispensaire (soin)
          4.Camp d'entrainement (amélioration martial)
          Autre. Sortir du village  
          """)
    choix = int(input("Votre choix : "))
    match choix:
        case 1:
            Action_forge(personnage)
        case 2:
            Action_amurie(personnage)
        case 3:
            Action_Dispensaire(personnage)
        case 4:
            Action_Camp(personnage)
        case _:
            print("Vous sortez du village.")
           


