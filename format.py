# Author: John 
# Date: Febuary, 12 2022
# This program is about how to format and output
firstname = 'John'
lastname = 'Li'
city = 'Markham'
province = 'Ontario'
#output =  'Hello '+ firstname + ' ' + lastname 
#output = 'Hello, {} {}'.format(firstname, lastname)
#output = 'Hello, {0} {1} in {2} '.format(firstname, lastname, city)
output = f'Hello, {firstname} {lastname} in {city} of {province}' 
print(output)