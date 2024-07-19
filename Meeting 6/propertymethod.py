class Person :
    def __init__(self,full_name,age):
        self.name = full_name
        self.age = age

    @property # only for private values
    def name(self):
        return self._name
    @name.setter # only for changing private values
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

person = Person("Vittorino Lucchesi", 20)
person.display_info()

person.name = "Patrick Tjen"
person.age = 0
person.display_info()