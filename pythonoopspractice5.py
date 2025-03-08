from abc import ABC, abstractmethod

class person(ABC):
    def __init__(self, favourite_car, favourite_bike):
        self.favourite_car = favourite_car
        self.favourite_bike = favourite_bike

    @abstractmethod
    def favourite_vehicles(self):
        print (f"my favourite vehicles are {self.favourite_car} and {self.favourite_bike}")


class student(person):
    def __init__(self, favourite_car, favourite_bike, favourite_brand):
        super().__init__(favourite_car, favourite_bike)
        self.favourite_brand = favourite_brand

    def favourite_vehicles(self):
          print (f"my favourite vehicles are {self.favourite_car} and {self.favourite_bike} of brand {self.favourite_brand}")

class professional(person):
    def __init__(self, favourite_car, favourite_bike, favourite_color):
        super().__init__(favourite_car, favourite_bike)
        self.favourite_color = favourite_color

    def favourite_vehicles(self):
          print (f"my favourite vehicles are {self.favourite_car} and {self.favourite_bike} of color {self.favourite_color}")

def favourite_vehicle_data (person):
    person.favourite_vehicles()

student1 = student('i7','M1','BMW')
professional1 = professional('i3','M2','BLUE')
favourite_vehicle_data(student1)
favourite_vehicle_data(professional1)

      