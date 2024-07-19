from Person import Person
from Employee import Employee # a class that is made in the file
from polymorph import show_info # needed function 

def Main():
    person = Person("John Doe",30)
    person.display_info()

    employee = Employee("Jane Doe",25,2134567)
    employee.display_info()

    show_info(person)
    show_info(employee)

if __name__ == "__main__":
    Main()

