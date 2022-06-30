#Author: John
#Date: Wendsday June 39
# This code is about json and how to make your code look better
import json

person_dict = {'first': 'John', 'last': 'Li'}
person_dict['City']='Toronto'

languages_list = ['CSharp','Python','JavaScript']

person_dict['languages']= languages_list

person_json = json.dumps(person_dict)

print(person_json)