# requirement1: ask your firstname, middle name, last name, and print out initial.
# requirement2: get a function call get_initial, and use it to extract initials for all the names
def get_initial(name):
     initial = name[0:1]
     return initial


first_name = input ('Enter your first name ')
first_name_initial = get_initial(first_name)

middle_name = input ('Enter your middle name ')
middle_name_initial = get_initial(middle_name)

last_name = input ('Enter your last name ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)