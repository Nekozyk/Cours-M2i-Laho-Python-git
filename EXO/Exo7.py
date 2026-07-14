random = __import__('random')

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

def Action_Joueur_combat():
    print("""Vous allez rentrer dans la caverne à cotés du village
            1.Attaquer
            2.Fuir comme un lache""")
    choix = int(input("Votre choix : "))
    return choix

def Combat(personnage={},ennemi={}):
    fuite = False
    while ennemi["PV"]>0 or personnage["PV"]>0:
       print("Vos pv sont de : ",personnage["PV"])
       if Action_Joueur_combat()==1:
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
       
   


"""
Arme=>type de des degats
attaque=> nombre de des
armure => CA
PV
bonus arme => bonus arme
combat => bonus de comat
"""
personnage = {"PV":10,"Arme":10,"Attaque":1,"Armure":10,"combat":1,"bonus arme":3,"argent":20}
kobolt =  {"NOM":"Kobolt" ,"PV":5,"Arme":6,"Attaque":1,"Armure":5,"combat":0,"bonus arme":0,"argent":2}
gobelin = {"NOM":"gobelin","PV":6,"Arme":6,"Attaque":1,"Armure":6,"combat":0,"bonus arme":0,"argent":3}
prix_arme = 10
prix_armure = 10
prix_soin =10
prix_entrainement = 100


while True:
    choix = 3
    if personnage["PV"] ==0:
        print("Vous avez échouer, on vous a secouru, vous vous reveillez au dispancère.")
        personnage["argent"] /=2
        choix=2
    else:
       print("""Vous êtes devant la caverne à cotés du village
                1.entrer dans la caverne
                2.retrouver au village pour se préparer
                3.Fuir comme un lache""")
       choix =  int(input("Votre choix"))

    match choix:
        case 1:
            print("""Vous allez enchainer 5 combats:
            -Une victoire vous donnera de l'argent
            -Un bonus d'argent vous sera octroyer si vous parvenez à la fin du donjon
            -Vous pouvez fuir entre chaque combat
            -Si vos PV tombent à 0 vous serez ramener au village avec une penalité de 50% de votre or""")
            nb_combat =0

            while nb_combat < 5:
             rencomtre_aleatoire = random.randint(1,2)
             if rencomtre_aleatoire == 1:
                   ennemy = kobolt
             else:
                   ennemy = gobelin

             fuite =  Combat(personnage,ennemy)

             if fuite:
              print("Vous avez fuit le combat")
              break

             if personnage["PV"]==0:
                break

             if ennemy["PV"]<=0:
                personnage["argent"]+=ennemy["argent"]
                nb_combat +=1
             else:
                break

            print("Vous êtes venu à bout des 5 combats vous recevez un bonus de 50 po")
            personnage["argent"]+=50

        case 2 :
            print("Vous êtes dans le village qui vous a engagé pour nettoyer le nid de monstre non loin")
            break
        case 3 :
            print("Vous fuyez en abondonnant le village qui vous a engagé. La honte vous poursuivra ")
            break
        case _:
            print("Vous ne savez pas comment ni pourquoi mais une enclume vous tombe dessus et vous tue!")
            break





