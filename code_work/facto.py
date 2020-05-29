val = int(input("please choose an int : "))

def factorial(val):
    if val < -1:
        return val * factorial(val + 1)
    elif val > 1:
        return val * factorial(val - 1)
    elif val == 0:
        return 1
    return val

print (factorial(val))