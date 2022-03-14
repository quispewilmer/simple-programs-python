# Following this tutorial: https://wiki.python.org/moin/SimplePrograms

import re
import sys
import glob
from time import localtime

# Output
print('Hello world!')

# Input assignment
name = input('Put your name: \n')
print('Hello, {name}'.format(name = name))

# For loop and enumerate function
products = ['Window', 'Pen', 'Pencil', 'Screen']
for i, description in enumerate(products):
    print('The product {product} has the ID {id}'.format(product = description, id = i))

# Fibonacci serie
parents, babies = (1, 1)
while babies < 100:
    print('This generations has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

# Functions
def greetings(name):
    print('Hello, {0}'.format(name))

greetings('Mark')
greetings('Paul')

# Regex
for test_string in ['555-1212', 'ILL-EGAL']:
    if(re.match(r'^\d{3}-\d{4}$', test_string)):
        print("{0} is a valid phone number".format(test_string))
    else:
        print("It's not a valid phone number.")

# Dictionaries and Generator Expression
prices = {'apple': 0.30, 'orange': 0.20}
my_purchase = {
    'apple': 2,
    'orange': 4
}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
for fruit in my_purchase)

print('I owe the grocer {0: 0.3f}'.format(grocery_bill))

# Command line
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum = {0}'.format(total))
except ValueError:
    print('Enter a valid integer argument.')

# Opening files
files = glob.glob('*.py')

for file in files:
    with open(file) as opened_file:
        for line in opened_file.readlines():
            print(line)

# Date and time
activities = {
    8: 'wake up',
    9: 'work',
    13: 'lunch',
    14: 'back to work',
    19: 'stop working',
    21: 'dinner',
    24: 'sleep'
}

time_now = localtime()
hour = time_now.tm_hour

for activity in sorted(activities.keys()):
    if hour < activity:
        print('The following activity at {0} is: {1}'.format(activity, activities[activity]))

# Tripple quoted Strings
REFRAIN = '''
{0} bottles of coca-cola on the wall,
{1} bottles of coca-cola,
take one down, pass it around,
{2} bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN.format(bottles_of_beer, bottles_of_beer, bottles_of_beer - 1))
    bottles_of_beer -= 1