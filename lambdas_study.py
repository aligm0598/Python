#Author: John
#Date: Tuesday July 19
#This code is anout lambdas and how to sort
presenters = [
    {'name': 'Micheal', 'age' : 52},
    {'name': 'John', 'age' : 14},
    {'name': 'Xuefan', 'age' : 52},
    {'name': 'Shannon', 'age' : 20},
]

presenters.sort(key = lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

presenters.sort(key = lambda item: (item['age']))
print('-- length --')
print(presenters)