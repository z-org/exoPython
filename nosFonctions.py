def tapezLettre ():
    boite = input("tapez les characteres")
    return boite

def tapezEntier ():
    boite = int(input("tapez un chiffre entier "))
    return boite

def tapezFloat ():
    boite = float(input("tapez un chiffre à virgule"))
    return boite



def tableMultiplication ( table ):
    multiplicateur = 1
    while multiplicateur <= 10:
        print (table * multiplicateur)
        multiplicateur = multiplicateur + 1

