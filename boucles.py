from random import randrange

#-----------------------------
phrase = "Bonjour a tous !"

for lettre in phrase:
    if lettre in "aeiou":
        print(lettre)



#-----------------------------
table = int(input("tapez un chiffre : "))
multiple = 1
while multiple <= 10:
    print (table * multiple)
    multiple = multiple + 1



#-----------------------------
chiffre = random.randrange(100)

trouver = False

while trouver == False :
    a = int(input("Entrez un chiffre : "))
    if a < chiffre:
        print("le chiffre est plus grand")
    elif a > chiffre:
        print("le chiffre est plus petit")
    else:
        print("Bravo !")
        trouver = True
