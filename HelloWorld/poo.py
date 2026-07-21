class TrainElectrique:
    pass

class Chaise:
    nb_pieds:int
    materiaux: str
    couleur: str
    def __init__(self,_nb_pieds,_materiaux,_couleur):
       self.nb_pieds = _nb_pieds
       self.materiaux=_materiaux
       self.couleur=_couleur

    def affiche(self):
        print(self.nb_pieds,self.materiaux,self.couleur)
    
    
chaise_a = Chaise(6,"metal","jaune devant maron derrière")
chaise_a.affiche()
#pour l'héritage
class fauteuille(Chaise):
    pass
