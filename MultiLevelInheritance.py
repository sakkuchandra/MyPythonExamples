class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()
