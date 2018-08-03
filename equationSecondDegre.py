import math
from nosFonctions import *
#on utilise notre fonction qui permet de recuperer un chiffre entier au clavier
a = tapezEntier()
b = tapezEntier()
c = tapezEntier()

#on sait que pour resoudre l'equation, on doit trouver le delta (google)

delta = (b*b) - 4*a*c #ici formule google
print("le delta = ", delta)

if delta > 0 : 
    print ("2 valeurs possible.")
    #si delta plus grand que 0 on que l'on a deux reponses et faut utiliser les formules suivantes 
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("x1 = ",x1," x2= ",x2)

elif delta == 0 :
    print ("1 valeur possible")
      #si delta plus grand que 0 on que l'on a 1 reponse et faut utiliser les formules suivantes 
    x1 = -b  / (2*a)

    print("x = ",x1)

else:
    print("pas de réponse.")
    