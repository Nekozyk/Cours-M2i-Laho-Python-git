#sauvegarde l'avancé du personnage dans le fichier personnage.csv
import csv
# exemple de données reçu {"PV":10,"Arme":6,"Attaque":1,"Armure":10,"combat":1,"bonus arme":0,"argent":20,"potions":1}
def Sauvegarde_perso(personnage):
    # ouvrir le fichier en mode écriture CSV
    fieldnames = ['PV', 'Arme', 'Attaque', 'Armure', 'combat', 'bonus arme', 'argent', 'potions']
    with open('personnage.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'PV': personnage["PV"],
            'Arme': personnage["Arme"],
            'Attaque': personnage["Attaque"],
            'Armure': personnage["Armure"],
            'combat': personnage["combat"],
            'bonus arme': personnage["bonus arme"],
            'argent': personnage["argent"],
            'potions': personnage["potions"]
        })
    