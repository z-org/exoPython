#on defini nos fonctions, chaque fonction comprend: 
#def nonDeFonction ():
#si on besoin que notre fonction nous donne une reponse on ecrit return plus la valeur a retourner

def tapezLettre ():
    boite = input("tapez les characteres")
    #ici on renvois la valeur contenue qui contient les charcteres tape
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

