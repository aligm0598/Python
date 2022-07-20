from unicodedata import name


class Presenter():
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        print(self.name)

presenter = Presenter('John')
presenter.say_hello()