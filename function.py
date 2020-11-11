def loading_screen():
  print("This page is loading...")

loading_screen()

#white space

def about_this_computer():
  print("This computer is running on version Everest Puma")
  print("This is your desktop")

about_this_computer()

def about_this_computer():
  print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()

#Parameters

def greet_customer(special_item):
  print("Welcome to Engrossing Grocers.")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
greet_customer("peanut butter")

def mult_two_add_three():
  number = 5
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three()

# Now, modify the function definition so that it has a parameter called number. Then delete the number = 5 assignment on the first line of the function.

# Pass the number 1 into your function call

def mult_two_add_three(number):
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(1)

#Multiple parameters

def greet_customer(grocery_store, special_item):
  print("Welcome to "+ grocery_store + ".")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
greet_customer("Starbucks", "Cold Brew")

#Keyword Arguments
def greet_customer(special_item, grocery_store="Engrossing Grocers"):
  print("Welcome to "+ grocery_store + ".")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
greet_customer("bananas")

#def greet_customer(special_item="bananas", grocery_store): # this is not valid
 # ...

#def greet_customer(special_item, grocery_store="Engrossing Grocers"): # this is valid
  #...

#return
def divide_by_four(input_number):
  return input_number/4

result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")

def create_special_string(special_item):
  return "Our special is " + special_item + "."
special_string = create_special_string("banana yogurt")

print(special_string)

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return  age
my_age = calculate_age (2049, 1993)
dads_age = calculate_age (2049, 1953)
print("I am "+ str(my_age) + " years old and my dad is " + str(dads_age) + " years old")


#MULTIPL RETURN VALUE

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit
low, high = get_boundaries(100, 20)
print(low, high)

#SCOPE

#If we try to run this code, we will get a NameError, telling us that 'special_item' is not defined. The variable special_item has only been defined inside the space of a function, so it does not exist outside the function.
def create_special_string(special_item):
  return "Our special is " + special_item + "."

#print("I don't like " + special_item)

#Variables defined outside the scope of a function may be accessible inside the body of the function:
header_string = "Our special is " 

def create_special_string(special_item):
  return header_string + special_item + "."
print(create_special_string("grapes"))

current_year = 2048
def calculate_age(birth_year):
  age = current_year - birth_year
  return age
print(calculate_age(1970))

#Review
your_boat = "Your Boat. "

def repeat_stuff (stuff,num_repeats = 10):
  return stuff * num_repeats  
lyrics = repeat_stuff("Row ",3) + your_boat
print(lyrics)
song = repeat_stuff(lyrics)
print(song)


#quiz
def update(new_value = 10):
  old_value = new_value
  return old_value
print(update(5))

time = "3pm"
mood = "good"

def report():
  print("The current time is " + time)
  print("The mood is " + mood)

print("Beginning of report")

report()