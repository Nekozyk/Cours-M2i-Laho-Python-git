import csv
class Perso:
     PV:10
     Arme:6
     Attaque:1
     Armure:10
     combat:1
     bonus_arme:0
     argent:20
     potions:1
     xp:0

     def __init__(self,pv,arme,Attaque,_armure,combat,bonus_arme,argent,potions,xp):
          self.PV           = pv
          self.Arme           =arme
          self.Attaque           =Attaque
          self.Armure           =_armure
          self.combat           = combat
          self.bonus_arme           =bonus_arme
          self.argent           =argent
          self.potions           =potions
          self.xp               =xp
          
     def Save(self):
    # ouvrir le fichier en mode écriture CSV
      fieldnames = ['PV', 'Arme', 'Attaque', 'Armure', 'combat', 'bonus arme', 'argent', 'potions','xp']
      with open('personnage.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'PV':  self.PV,         
            'Arme': self.Arme,     
            'Attaque':   self.Attaque,
            'Armure':  self.Armure ,  
            'combat':    self.combat,
            'bonus arme':self.bonus_arme ,
            'argent':   self.argent, 
            'potions':  self.potions,
            'xp' : self.xp
        })
     def Load(self):
          with open('names.csv', newline='') as csvfile:
           reader = csv.DictReader(csvfile)
          for row in reader:
               self.PV         = row['PV']
               self.Arme       = row['Arme']
               self.Attaque    =row['Attaque']
               self.Armure     =row['Armure']
               self.combat     =row['combat']
               self.bonus_arme =row['bonus arme']
               self.argent     =row['argent']
               self.potions    =row['potions']
               self.xp         =row['xp']