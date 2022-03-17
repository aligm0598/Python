#Author: John
#Date: March 16 2022
# This program is about how to use while loop and for loop
people = ['Michael','Michelle','Shannon','John']

index = 0
while index < len(people):
    print(people[index])
    print(index)
    index = index + 1

print(len(people))
for name in people:
     print(name)
