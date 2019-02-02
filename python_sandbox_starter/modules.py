# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core modules
import datetime
from datetime import date
from time import time

#Pip module 
from camelcase import CamelCase

# today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()
# print(timestamp)

c = CamelCase()
print(c.hump('hello there world'))


