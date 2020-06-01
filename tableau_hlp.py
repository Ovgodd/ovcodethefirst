lil = open("c1.txt","r")
big = open("c2.txt","r")
#rentre la donnée manipulable - comment la rendre manipulable

l = []#création liste vide petit(l) et grand(b) rectangle
b = []


for i in lil:  #transformation en liste avec .split() du fichier txt pour le mettre dans la variable créer plus tôt
    l+=i.split() 
for j in big:
    b+=j.split()

def square(l,b,bx,by):
    lx = 0#def position ligne petit carré à 0
    while ly < len(l):
        ly = 0#def position colonne petit carré à 0
        while ly < len(l): #tant que ma position de colonne ( exemple 0 )est inferieur au nombre d'élement dans mon tableau ( 9 elements pour le petit)
            if (l[lx][ly] != b[bx+lx][by+ly]): #si ma valeur retrouvée dans le petit carré est différente de la valeur retrouvée dans le grand.
                return False #retournons faux
            ly += 1 #incrémentation pour éviter la boucle infinie
        x += 1
    return true #boucle terminée retournons vrai.

def check(l,b):

    bx = 0  #bx = ligne grand carré
    while  bx < len(b): #tant que ma position de bx est inferieur au nombre d'élément dans mon tableau( grand )
        by = 0
        while  by < len(b): 
            if(b[bx][by] == l[0][0]): #si ma valeur retrouvée en ligne/colonne du grand carré est = a la position 0 0 de mon petit carré ( en l'occurence 1 )
                print(by,bx)
                return True #retounons vrai, valeur : OK
                
            by +=1
        bx += 1

    return False #sinon retournons faux, la boucle continue
check(l,b)

    


    


# boucle b ligne , bx
#   boucle b colonne , by
#        if vérifier que dans l[lx][ly]( itinié a 0 ) == b[bx][by]
#          #  boucle sur l : lx
#          #   boucle sur l : ly
#          #     si b =! l[lx],ly]
#          #        break
#          #     end
#          #   end 
#          #  end
#          #  BON!! return position bx by
#       end
#   end
#end
# PAS DE RESULTAT



#for k in b:
    #if (b[bx], b[by] != l[lx], b[bx]):
        #bx += 1
        
            

        