import math
from nosFonctions import *

a = tapezEntier()
b = tapezEntier()
c = tapezEntier()

delta = (b*b) - 4*a*c
print("le delta = ", delta)

if delta > 0 :
    print ("2 valeurs possible.")
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("x1 = ",x1," x2= ",x2)

elif delta == 0 :
    print ("1 valeur possible")
    
    x1 = -b  / (2*a)

    print("x = ",x1)

else:
    print("pas de réponse.")
    