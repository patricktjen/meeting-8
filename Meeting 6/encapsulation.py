class Person :
    def __init__(self):
        self.name = "Vittorino Lucchesi"
        self.age = 20
    
    @property # only for private values
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value > 0:
            self._age = value
        else:
            return ValueError("Age cannot be negative")
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person()
person.display_info()

person.name = "Patrick Tjen"
person.age = 1
person.display_info()