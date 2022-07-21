from lib2to3.pygram import pattern_symbols


class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello '+ self.name)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to' + self.school)
    def say_hello(self):
        #super().say_hello()
        print('I like hockey')
    def __str__(self):
        return f'{self.name} attends {self.school}'

student = Student('John', ' UPS')
print(student)
#student.say_hello()
#student.sing_school_song()

print(f'Is this a student?{isinstance(student, Student)}')
