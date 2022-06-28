#Author: John
#Date: Monday June 27
#This code Tells Demo what it wants printed and what color it wants printed. This code has to functions display and sayHello.   
from pip._vendor.colorama import init, Fore

def display(message,is_warning=False): 
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE+message)

# add another function call sayHello, print 'hello' + message
def sayHello(message,is_warning=False):
    if is_warning:
       print(Fore.YELLOW + message)
   
