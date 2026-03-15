class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    def print_passengers(self):
        if self.passengers != []:
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("No passenger")

nick = Human("Nick")
car = Auto("Mercedes")
car.add_passenger(nick)
car.print_passengers()

marco = Human("Marco")
car = Auto("Toyota")
car.add_passenger(marco)
car.print_passengers()