from email import message


def print_hello(name:str) -> str:
    """
    Returns a greeting 

    parameter:
        name (str): The name of the person

    Returns:
        The cool message
    """

    name= input('What is your name')
      
first_name = input('What is your first name? ')

last_name = input('What is your last name? ')

print('Hello, ' + first_name.capitalize() +' '+ last_name.capitalize())



# Dad's challeng, ask for a name and use print_hello() to print out the message
