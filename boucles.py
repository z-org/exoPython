#depuis la bibliotheque random , on importe la fonction ( formule) randrange
#qui permet de recuperer un chiffre aleatoire  
from random import randrange

#-----------------------------
#exemple 1 

#on cree une variable phrase qui contient la chaine de caractere "Bonjour a tous !"
phrase = "Bonjour a tous !"
#la boucle for permet de parcourir la phrase en recuperant chaque caractere et la stoque temporairement dans lettre
for lettre in phrase:
    #on compare la lettre recuperee avec la liste de voyelles 
    if lettre in "aeiou":
        print(lettre)



#-----------------------------

#input permet de demander de taper quelque chose au clavier 
#ici, un entier (int)
#on stoque la valeur entree dans table 
table = int(input("tapez un chiffre : "))
multiple = 1
#tant que la variable multiple est plus petit ou egale a 10
while multiple <= 10:
    #on affiche la multiplication de table choisie avec son mutiplicateur
    print (table * multiple)
    #on augmente a chaque tour de variable multiple +1
    multiple = multiple + 1



#-----------------------------
#demande a randrange de nous donner un chiffre aleatoire compris 
#entre 0 et 99 puis on stoque le resultat dans chiffre


chiffre = random.randrange(100)
#on cree une variable boolean qui vaut faux 
trouver = False

# tant que trouver est = a faut, on continue la boucle
while trouver == False :
    a = int(input("Entrez un chiffre : "))
    if a < chiffre:
        print("le chiffre est plus grand")
    elif a > chiffre:
        print("le chiffre est plus petit")
    else:
        print("Bravo !")
        #si on a trouve, il faut penser a changer la valeur de notre "flag" trouver qui passe a vrai
        trouver = True
