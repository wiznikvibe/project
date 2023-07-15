from src.person import Person
from src.car import Car

# For scripting file to desginate the starting point
if __name__ == '__main__':
    person1 = Person("Nikhil", "Shetty", 23, 'Data Scientist')
    person1.display_info()

    car1 = Car("Range Rover", 2023, "EV", 12550000)
    car1.display_info()