#SUDO BACKTRACK METH

sudo = open("cs.txt","r")  
s = []

for t in sudo:          #import fichier texte en liste
    s+=t.split()

for i in range(len(s)): #remplacement des caractères spéciaux pour avoir une liste "propre"
    s[i]=s[i].replace("|","")
    s[i]=s[i].replace("_","0")
s.pop(3) #suppression des caractères spéciaux en position 4 et 7.( la liste était : 'xxxxxxxxx','xxxxxxxxx',xxxxxxxxx,'---+---+---') > suppression ---+---..
s.pop(6)

def print_s(su): # création fonction pour retravailler la liste en grille plus exploitable

    for i in range(len(su)):#pour i dans la range de toute la longueur de su(tableau suddoku)
        if i % 3 == 0  and i != 0:#si le reste de ma division de i ( exemple 3) est = a 0 ET que i != 0 > si nous ne mettons pas i!=0 on aura "-----" au dessus
                                                                                                                #du sudo
            print("- - - - - - - - - - - - ")

        for j in range (len(su[0])): #pour j dans la range de toute la longeur de la premiere ligne (index0) du sudo
            if j % 3 == 0 and j != 0:#si le reste de ma division de i ( exemple 6) = 0 etc.. 
                print(" | ", end="")#print "|" cela va imprimer après les index 2 et 5 "|". end="" > pas de "/n"du coup pas de retour à la ligne, et le sudo s'affiche bien.

            if j == 8: #si notre j est = a 8 > 8 = notre range sudo ( 0 1 2 3 5 6 7 8) > rappel la 1ere valeur d'une liste est = a 0.
                print(su[i][j]) 
            else:
                print((su[i][j]) + " ",end="") # imprimer le sudoku en entier avec chaque valeur espacée. end = "" > evite le passage à la ligne

print_s(s)
