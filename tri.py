first_demand = input("please enter intergers separated by space : ")
user_list = first_demand.split()

liste = user_list

def tri_select(liste):
    L = len(liste)

    for i in range(L):
        for j in range(0, L-1):
            if liste[j] < liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

    return liste

print(tri_select(liste))