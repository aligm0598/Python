#Author: John
#Date: March 2 2022
# This program is about how to use dictionary 
dad = {}
dad['fist_name'] = 'Guangming'
dad['last_name'] = 'li'
dad['age'] = 52

mom = {}
mom['fist_name'] = 'Michelle'
mom['last_name'] = 'li'
mom['age'] = 52

sister = {}
sister['fist_name'] = 'Shannon'
sister['last_name'] = 'li'
sister['age'] = 19

brother = {}
brother['fist_name'] = 'John'
brother['last_name'] = 'li'
brother['age'] = 13

family = []
family.append(dad)
family.append(mom)
family.append(sister)
family.append(brother)
family_print = family[0:3]
print(family_print)