class Student:
    university = "Skillwill"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, increment):
        self.grade += increment


student = Student("Mariam", 50, 21)
print(student)
print("student is passing:", student.is_passing)

student.increase_grade(20)
print("after grade increasing:", student)
print("student is passing", student.is_passing)

