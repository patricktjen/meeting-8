class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self._employee_id = employee_id
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self._employee_id}")

employee = Employee("Yoneda Aika",24,2122100361)
employee.display_info()
