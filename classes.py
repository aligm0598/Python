#Author:John
#Date:Wednesday July 20
#This code is about classes
class Presenter():
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        print(self.name + ' says hello')

john = Presenter('John')
john.say_hello()

michael = Presenter('Michael')
michael.say_hello()