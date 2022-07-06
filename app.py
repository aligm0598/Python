#Author: John
#Date: Wed Jul 6
#This program is about hiding my passwords 
from ast import Pass
from dotenv import load_dotenv
load_dotenv()
import os

key = os.getenv('Key')

print(key)