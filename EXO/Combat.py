random = __import__('random')
from Action_Joueur import Action_Joueur_combat
def Attaque(CA,bonus):
    dice =   random.randint(1,20)
    if (dice+bonus) > (CA) and dice > 1:
        return True
    else:
        return False

def Degat(nombre_des=1,type_des=6,bonus=0):
    dice=0
    for i in range(nombre_des):
        dice +=   random.randint(1,type_des)
    return (dice+bonus)

def Combat(personnage={},ennemi={}):
    fuite = False
    while ennemi["PV"]>0 or personnage["PV"]>0:
       print("Vos pv sont de : ",personnage["PV"])
       if Action_Joueur_combat(ennemi["NOM"])==1:
                #combat tour par tour 
           print("Vous attaquez ",ennemi["NOM"])
           if Attaque(ennemi["Armure"],personnage["combat"]):
               print("attaque réeussi calcul des dégats.")
               degat = Degat(personnage["Attaque"],personnage["Arme"],personnage["bonus arme"])
               ennemi["PV"]-=degat
               print("Vous avez infligé ",degat," il reste ",ennemi["PV"]," à l'ennemi" )
           else:
                print("votre attaque a échoué.")

           if ennemi["PV"]>=0:
               print(ennemi["NOM"],"va repliquer")
               if Attaque(personnage["Armure"],ennemi["combat"]):
                print("attaque réeussi calcul des dégats.")
                degat = Degat(ennemi["Attaque"],ennemi["Arme"],ennemi["bonus arme"])
                personnage["PV"]-=degat
                print("vous avez pris ",degat," degats"," il vous reste ",personnage["PV"] )
               else:
                print("l'attaque ennemi a échoué.")
           else:
               print(ennemi["NOM"],"est mort")
               break
       else:
           fuite=True
           break
    return fuite