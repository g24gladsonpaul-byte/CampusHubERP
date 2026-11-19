
from app.core.descriptors import Name, Email, Age
from app.core.abc_interfaces import Person


class Student(Person):
    name = Name()
    email = Email()
    age = Age()

    def __init__(self, student_id, name, age, email, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department
        }
