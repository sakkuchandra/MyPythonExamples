#self is a pointer which stores the object created in the #programme

class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')


class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')



# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()
