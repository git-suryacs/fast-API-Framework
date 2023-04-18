class Student:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greetings(self):
        return f'Hello! I am {self.first_name} {self.last_name}'

student_1 = Student('Surya','CS')
student_2 = Student('John','Miller')


print(student_1.greetings())
print(student_2.greetings())