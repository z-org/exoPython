#on cree une variable qui egal a 5
boite = 5

#si la variable est plus grande que 10 

#on affiche plus grand
if boite > 10 :
    print("plus grand")
#ou si la variable (boite) est plus petite que 10
#on affiche plus petit 
elif boite < 10 :
    print("plus petit")
#en dernier recourt c'est que la variable est egale
else:
    print("egal")


#------------------
#exemple 2


#on garde le reste de division de 52 par (le modulo )
#on le stock dans variable ( boite ) ( endroit ou stock un resultat )

#si le contenu de la variable est egale à zero
# attention double = (==) quand on compare 2 elements 

boite = 52 % 2

if boite == 0 :
    print("52 est un chiffre paire")