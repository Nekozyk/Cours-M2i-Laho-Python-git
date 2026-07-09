nombre_un = float(input("Entrez un nombre : "))
nombre_deux = float(input("Entrez un autre nombre : "))

la_somme = nombre_un + nombre_deux

print("La somme de", nombre_un, "et", nombre_deux, "est égale à", la_somme)

la_difference = nombre_un - nombre_deux
print("La différence de", nombre_un, "et", nombre_deux, "est égale à", la_difference)

le_quotient = nombre_un / nombre_deux
print("Le quotient de", nombre_un, "et", nombre_deux, "est égale à", le_quotient)
le_quotient_entier = nombre_un // nombre_deux
print("Le quotient entier de", nombre_un, "et", nombre_deux, "est égale à", le_quotient_entier)

le_modulo = nombre_un % nombre_deux
print("Le modulo de", nombre_un, "et", nombre_deux, "est égale à", le_modulo)

le_produit = nombre_un * nombre_deux
print("Le produit de", nombre_un, "et", nombre_deux, "est égale à", le_produit)

egalite = nombre_un == nombre_deux
print("L'égalité de", nombre_un, "et", nombre_deux, "est", egalite) 
different = nombre_un != nombre_deux
print("La différence de", nombre_un, "et", nombre_deux, "est", different)
#operateurs de comparaison
superieur = nombre_un > nombre_deux
print("Le nombre", nombre_un, "est supérieur à", nombre_deux, ":",  superieur)
inferieur = nombre_un < nombre_deux  
print("Le nombre", nombre_un, "est inférieur à", nombre_deux, ":", inferieur)
#operateurs logiques
possede_cartes_bibliotheque = True
argent = 25
age = int(input("Entrez votre âge : "))
est_mineur = age < 18