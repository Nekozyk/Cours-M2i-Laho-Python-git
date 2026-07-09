#structure conditionnelle
age = int(input("Entrez votre âge : "))
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous n'êtes pas majeur.")    

statut = ""

if age < 18:
    statut = "mineur"
else:
    statut = "majeur"   


statut = "majeur" if age >= 18 else "mineur"

print("Vous êtes", statut)

#structure conditionnelle avec plusieurs conditions

choix = input("Entrez un choix (1, 2 ou 3) : ")
match choix:
    case "1":
        print("Vous avez choisi l'option 1.")
    case "2":
        print("Vous avez choisi l'option 2.")
    case "3":
        print("Vous avez choisi l'option 3.")
    case _:
        print("Choix invalide.")    

#structure itérative


while age < 18:
    print("Vous êtes mineur.")
    age += 1
else:
    print("Vous êtes majeur.")

for i in range(5):
    print("Itération", i) 

while True:
    choix = input("Entrez un choix (1, 2 ou 3) : ")
    match choix:
        case "1":
            print("Vous avez choisi l'option 1.")
        case "2":
            print("Vous avez choisi l'option 2.")
        case "3":
            print("Vous avez choisi l'option 3.")
        case _:
            print("Choix invalide.")
            break