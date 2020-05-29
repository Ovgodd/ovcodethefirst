user_val = input("please choose a sentence : ")
last_val = ""

for i in range(len(user_val)):
    char=user_val[i]
    if ( i % 2 ) ==  1:
        char=char.upper()
    last_val = last_val+char


print(last_val)