class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.emp_id}, Salary: ${self.salary:.2f}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}, Grade: {self.grade}"


class PersonInfo(Employee, Student):
    def __init__(self, name, age, emp_id, salary, student_id, grade):
        Employee.__init__(self, name, age, emp_id, salary)
        Student.__init__(self, name, age, student_id, grade)

    def __str__(self):
        return f"{Employee.__str__(self)}, {Student.__str__(self)}"


# Create an instance of PersonInfo
person_info = PersonInfo("John", 30, "E123", 50000, "S456", "A")

# Access the attributes and print details
print(person_info)
