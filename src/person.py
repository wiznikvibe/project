class Person: 

    def __init__(self, name, last_name, age, designation):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.designation = designation
    
    def display_info(self):
        print(f"Name: {self.name} {self.last_name} \n Age: {self.age} \n Job: {self.designation} \n")