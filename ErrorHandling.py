#Author: John
#Date: Feburary 16 2022
# This program is about how to do error handling 
number_a = input('Enter first number ')
number_b = input('Enter second number ')

try:
    print(int(number_a) / int(number_b))
except ZeroDivisionError as e:
    print('Please do not use 0 as the second number')
except ValueError as e:
    print('Please do not use other characters')
finally:
    print('Finished')
