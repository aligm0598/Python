#Author: John
#Date: february 22 2022
#This program is about how to use conditions  
cost = input('How much money did you spend? ')
cost = float(cost)

if cost >=  1.00:
    tax = 0.7
    #print('You spent: ' + str(cost) + ', your tax rate is: ' + str(tax))
else:
     tax = 0
     
print('You spent: ' + str(cost) + ', your tax rate is: ' + str(tax))