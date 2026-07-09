mon_texte = "je suis un texte"
nb_caractere = len(mon_texte)

montexte_majuscule = mon_texte.upper()

for i in range(nb_caractere):
    print(mon_texte[i])
    if mon_texte[i].upper() in "AEYUIO":
        print("Voyelle")
    else:
        print("Consonne")

recup = mon_texte.capitalize()
print(recup)

fruits = "pomme, banane, cerise, orange"

for fruit in fruits.split(","):
    print(fruit)

    from math import pi

nbpi = pi

print(f"Nombre de pi : {nbpi:.2f}")

