#Author:John
#Date: Saturday, July, 9
# This code is about decorators
def logger(func):
    def wrapper():
        print('Logging exucution')
        func()
        print('Done logging')
    return wrapper

@logger
def sample():
    print('-- Inside sample function')

sample()