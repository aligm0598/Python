# Author: John 
# Date: Friday June 24
# This code is about parameterized functions. This code asks for your first name and will give you your intial if.
# Dad's challenge: also check last name and return initial for first and lastname
def get_initial(name, force_uppercase= True): 
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial 

First_name = input ('Enter your first name: ')
First_name_initial = get_initial(force_uppercase= False, name=First_name,)

Last_name = input ('Enter your last name: ')
Last_name_initial = get_initial(force_uppercase= False, name=Last_name,)

print('Your initial is: ' + First_name_initial + Last_name_initial)