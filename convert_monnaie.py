req_one = int(input("Hello what is the amount that you want to convert : "))
req_two = str(input("what is your currency ? "))
req_three = str(input("what currency do you want ? exemple \"dollars\" : "))
req_four = float(input("what is the price( cours )of the currency that you want ? you can check it on google exemple : \"1 dollars to pound price\" : "))

def monney(num1=int(req_one),num2=float(req_four)):
    return round(num1 * num2)

print ("You want to convert " + str(req_one) + " " + str(req_two) + ".")
print ("you will have : " + str(monney()) + " " + str(req_three) + ".")
