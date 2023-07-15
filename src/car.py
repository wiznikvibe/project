class Car:
    def __init__(self, model, year, fuel_type, price):
        self.model = model 
        self.year = year
        self.fuel_type = fuel_type
        self.price = price 

    
    def display_info(self):
        print(f"This {self.model} was released in the year {self.year}")