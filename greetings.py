class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = None

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def welcome(self):
        return f"Welcome to Albert School, {self.first_name}!"

    def enroll(self, classroom):
        self.classroom = classroom
        return f"{self.full_name()} joins {self.classroom}."

    def is_enrolled(self):
        return self.classroom is not None

    def farewel(self):
        return f"See you soon, {self.first_name}!"


# Create a student object
student = Student("Tuka", "Bade")

# Use its methods
print(student.welcome())
print(student.is_enrolled())
print(student.enroll("MSc 1 Data"))
print(student.is_enrolled())
