class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class mixin:
    def attributes(self):
        attributes = vars(self)
        return ', '.join(f"{key}: {value}" for key, value in attributes.items())


class Student(Person, mixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

    def __str__(self):
        return self.attributes()


person = Person("Mariam", "Pirosmanishvili", 21)

student = Student("Mariam", "Pirosmanishvili", 21, "Skillwill")
print(student)
