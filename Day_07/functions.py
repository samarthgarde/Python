    # Syntax: 

    # def function_name(parameters): 
    # # Block of code 
    # return value 

# Creating a Function
def my_function():
  print("Hello from a function")

  my_function()

# Arguments
# Information can be passed into functions as arguments.

def my_function(name):    # name is parameter
  print(name + "End_point")

my_function("email")   # email is argument
my_function("first_name")
my_function("last_name")

def my_function(country = "india"):
  print("i am from ", country)

my_function("pakistan")   # i am from pakistan
my_function("israil")
my_function("japan")
my_function("tokiyo")

def my_function(animal,name,color):
  print("I have a", animal)
  print("my",animal + "s name is",name)
  print("my dog color is", color)

my_function(name= "Buddy", animal = "dog", color="black")

# Using *args to accept any number of arguments

def my_function(*kids):      # this is for *args argument
  print("The youngest child is " + kids[2])    #getting indexing

my_function("Emil", "Tobias", "Linus")

# Using **kwargs to accept any number of keyword arguments

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Combining *args and **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# single means we are passing arbitrary number of positinal arguments
# Double ** means we are passing arbitrary number fo keyword argument
# the  * has the data type of tuple
# the ** has the data type of dictionary

# Local variable VS Gloabl variable

print("-----------------")

# Function within Functions
def f1():
    s = 'I love python'
    def f2():
        print(s)
        
    f2()
f1()

print("-----------------")

# Function with Return Value
def add(a,b):
  return a + b

result = add(2,4)
print(result)

# Default Arguments
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sam")

# Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


# Basic Decorator
def changecase(func):            # this is the main function
  def myinner():                 # this is the sub function
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction()) 

print("--------------")

# Even_Odd number using function

def odd_even():
   num = int(input('Enter a number'))
   if num % 2 == 0:
      print("Even")
   else:
      print("odd")
      return num
   
user = odd_even
print(user)