from Person import Person

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self._employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self._employee_id}")