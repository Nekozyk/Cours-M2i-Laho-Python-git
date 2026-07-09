nombre_a=10
nombre_b=0
try:
    resultat = nombre_a / nombre_b
    print("Le résultat est :", resultat)

except Exception as patronum:
    print("Une erreur s'est produite :", str(patronum))
finally:
    print("Expecto patronum !")
