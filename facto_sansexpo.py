val = int(input("please choose an int : "))

def factorial(val):
    if val < -1:
        return val * factorial(val + 1)
    elif val > 1:
        return val * factorial(val - 1)
    elif val == 0:
        return 1
    return val



a = str(factorial(val))
reverse_fac = a[::-1]
b = ''

i = 0
while ( i < len(reverse_fac)):
    b += reverse_fac[i]
    if ((i + 1 ) % 3 == 0):
        b += ','

    i += 1
print(b[::-1])
#but : ajouter virgule, 1,405,006...
#créer var pour transformer factorial val en str et l'inverser. revers_fac
#crée var ','
    #boucle while i revers_fac
        #if i % 3 == 1:
            #var[i] += var','
#reverse ensuite une nouvelle fois le resultat pour avoir le 1,405,006
