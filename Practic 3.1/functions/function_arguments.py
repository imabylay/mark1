# Arguments

# 1
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# 2
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument



# 3 Number of Arguments should be equal
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #correct
my_function("Emil") #incorrect


# 4 Default Parameter Values - for empty calling
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# 5 Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


# 6 Positional Arguments - The order matters with positional arguments:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
my_function("Buddy", "dog")


# 7 Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# 8 Passing Different Data Types
# list 
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# dictionary 
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


# 9 Positional-Only and Keyword-Only
# positional-only arguments, add , / 
# only keyword arguments, add *,
# Combining 
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


# 10 Unpacking Arguments
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)