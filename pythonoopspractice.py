class State:
    def __init__(self, city, population):
        self.city = city
        self.population = population

    def call_city(self):
        print(self.city)

    def call_population(self):
        print(self.population)

# indian_state = State('bangalore',100000)
# indian_state.call_population()

class city(State):
    def __init__(self, city, population, state):
        super().__init__(city, population)
        self.state = state
    
indian_city = city('bangalore', 100000, 'karnataka')
indian_city.call_population()
indian_city.call_city()


