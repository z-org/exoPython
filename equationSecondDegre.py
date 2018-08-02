import math
from nosFonctions import *

a = tapezEntier()
b = tapezEntier()
c = tapezEntier()

delta = (b*b) - 4*a*c
print("le delta = ", delta)

if delta > 0 :
    print ("2 valeurs possible.")
    
    math.sqrt(delta)

elif delta == 0 :
    print ("1 valeur possible")
else:
    print("pas de réponse.")
    