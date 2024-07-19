class Person : # class
    def __init__(self,name,age):
        self.name = name # attribute / object
        self.age = age # attribute / object
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# pemanggilan kelas
person = Person("Vittorino Lucchesi",20)
person.display_info()

