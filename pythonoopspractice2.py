class Person:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def __add__(self, other):
        return Person(self.age + other.age, self.weight + other.weight)
    
    def __str__(self):
        return f"Age: {self.age}, Weight: {self.weight}"
                
person1 = Person(12, 56)
person2 = Person(20, 80)

# Added __str__ method to properly print the result of the addition
print(person1 + person2)