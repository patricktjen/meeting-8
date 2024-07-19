class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print((f"Name: {self.name}, Age: {self.age}"))

# constructor bersifat memaksa
person = Person("Vittorino Lucchesi",20)
person.display_info()



