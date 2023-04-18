class Student:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greetings(self):
        return f'Hello! I am {self.first_name} {self.last_name} from parent class'


class CollegeStudent(Student):
    def __init__(self,first_name,last_name,major):
        super().__init__(first_name,last_name)
        self.major = major

    def greetings(self):
        return f'{self.first_name} is a college student'

class NonCollegeStudent(Student):
    def __init__(self,first_name,last_name,future_job):
        super().__init__(first_name,last_name)
        self.future_job =future_job

student_1 = CollegeStudent('Surya','CS','Computer Science')
student_2 = Student('John','Miller')
student_3 = NonCollegeStudent('Rohit','Miller','Pilot')



print(student_1.greetings())
print(student_2.greetings())
print(student_1.major)
print(student_3.future_job)