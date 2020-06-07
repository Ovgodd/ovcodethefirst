#class disponible_car
#Layer of absaction : disponible car, car price, too add a car, to lend a car
#class customer
#choose a car, return a car

class car:

    def __init__(self,listOfCars):
        self.availableCars = listOfCars

        def disponibleCar(self):
            print()
            print("Avaiables Cars : ")
            for cars in self.availableCar:
                print(cars)

        def addCar(self, returnedCar):
            self.availableCar.append(returnedCar) 

        def lendCar(self, chooseCar):
            if chooseCar in availableCar:
                print("ok you have rent a car")
                self.availableCar.remove(chooseCar)

        def prices(self,dayPrice):
            for price in dayPrice:
                customerPrice = dayPrice * prices
        
        


class customer:

    def chooseCar(self):
        print("please what car do you want ? ")
        self.cars = input()
        return self.cars
        

    def returnedCar(self):
        print("please what car do you want to return ? ")
        self.cars = input()
        return self.cars

    def dayPrice(self):
        print("how many day do you want your car ? ")
        self.cars = input()
        return self.cars

Car = car(['Hatchback','Sedan','SUV'])
Customer = customer()

while True:
    print("Enter 1 to display the car ")
    print("Enter 2 to request a car")
    print("Enter 3 to return a car")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        Car.disponibleCar()
    elif userChoice is 2:
        wantedCar = customber.chooseCar
        customer.lendCar(chooseCar)
    elif userChoice is 3:
        returnIt = customer.returnedCar()
        Car.addCar(returnedCar)
    elif userChoice is 4:
        quit()