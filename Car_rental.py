#class car,
#layer of abstraction : disponible car / fare details / fare calculs
#object Car

class Car:
    def __init__(self):
        self.carFare = {'Hatchback' : 30, 'Sedan':50, 'SUV': 100}  #car prices listed with names

    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback : $",self.carFare['Hatchback'])
        print("Sedan : $",self.carFare['Sedan'])
        print("SUV : $",self.carFare['SUV'])

    def calculateFare(self, typeOfCar, numberOfDays):#calculate the fare depending of the cars and the days that user choice

        return self.carFare[typeOfCar] * numberOfDays


car = Car()
while True:
    print("Enter 1 to display the fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.displayFareDetails()
    if userChoice is 2:
        print("enter the type of car would you like to want : ")
        typeOfCar = input()
        print("please enter the numbers of days would you like to have this car : ")
        numberOfDays = (int(input()))
        fare = car.calculateFare(typeOfCar, numberOfDays)
        print("total payable amount : $",fare)
        print("Thank you!")
    elif userChoice is 3:
        quit()
