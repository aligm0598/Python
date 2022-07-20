#Author:John
#Date:Wednesday July 20
#This code is about classes
class Presenter():
    def __init__(self, name):
        self.name = name

    def name(self):
         return self._name
    
    def name(self, value):
        self._name = value

john = Presenter('John')
print(john.name)

michael = Presenter('Michael')
print(michael.name)

    