class Employee:
    company_name = 'Futurense'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show(self):
        print('Employee:', self.name, self.salary, self.company_name)

emp1 = Employee("Saurav", 12000)
emp1.show()

emp2 = Employee("Piyush", 10000)
emp2.show()