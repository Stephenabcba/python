num1 = 42 # variable declaration, numbers
num2 = 2.3 # variable declaration, numbers
boolean = True #variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuples
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, list access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # log statement, dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary change value
print(fruit[2]) # tuples access value

# conditional
if num1 > 45: # if statement
    print("It's greater") # log statement
else: # else
    print("It's lower") # log statement

if len(string) < 5: # if
    print("It's a short word!") # log statement
elif len(string) > 15: # else if
    print("It's a long word!") # log statement 
else: # else
    print("Just right!") # log statement

# for loop
for x in range(5):
    print(x) # log statement
for x in range(2,5):
    print(x) # log statement
for x in range(2,10,3):
    print(x) # log statement

# while loop
x = 0 # start
while(x < 5):
    print(x) # log statement
    x += 1

pizza_toppings.pop() # list delete value
pizza_toppings.pop(1) # list delete value

print(person) # log statement
person.pop('eye_color') # dictionary delete value
print(person) # log statement

# for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue # continue
    print('After 1st if statement')
    if topping == 'Olives':
        break # break

# function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'