class Presenter():
    def __init__(self, name):
        self.name = name

    def name(self):
         return self._name
    
    def name(self, value):
        self._name = value

presenter = Presenter('John')
print(presenter.name)


    