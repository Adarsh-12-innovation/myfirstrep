class vehicle:
    def __init__(self,id):
        self.id = id

    def call_speed(self):
        print(f"the speed of the car is {self.id}")

car = vehicle(23)

car.id()