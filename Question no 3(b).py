class Person:
    def __init__(self, name, address, number):
        """Constructor of Person"""
        self.name = name
        self.address = address
        self.number = number

    def get_Person(self):
        """Returns the name of a person"""
        return self.name

    def get_all_detail(self):
        """Returns all the details of person"""
        return "HI! My name is " + self.name + " and I live at " + self.address

    def get_contact(self):
        """Returns the contact of the person"""
        return self.number


class Employee(Person):
    def __init__(self, name, address, number, salary, department):
        """Constructor of Employee"""
        Person.__init__(self, name, address, number)
        self.salary = salary
        self.department = department

    def get_contact(self):
        """Checks if the number is none and returns the contact of the 
        person"""
        if self.number == None:
            return "Does not have a number"
        else:
            return self.number

    def change_number(self, new_number):
        """method for CHANGING the number of the person"""
        self.number = new_number

    def change_address(self, addr):
        """method for CHANGING the address of the person """
        self.address = addr

foo = Person("Ram", "Kamalpokhari", "9812121212")
print(foo.get_all_detail())
print(foo.get_contact())
bar = Employee("Rabi", "Gaushala", "9836699636", "40000", "HR")
print(bar.get_all_detail())
bar.change_address("Koteshwor")
print(bar.get_all_detail())
