# you can specify that a function can have only positonal arguments,or only keyword arguments.

# To specify that a function can have only one positional arguments add , / after the arguments:

def my_function(x, /):
    print(x)

my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

# Example
def my_function(x):
    print(x)

my_function(x=3)


# But when adding the , / you will get an error if you try to send a keyword argument:

# Example


# def my_function(x, /):
#   print(x)

# my_function(x = 3)

# keyword only arguments
# to specify that a function can have only keyword arguments, add *, before the arguments:

# Example
def my_function(*,x):
    print(x)

my_function(x=3)

# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(x):
  print(x)

my_function(3)

# But with the *, you will get an error if you try to send a positional argument:


# def my_function(*, x):
#   print(x)

# my_function(3)

# combine Positional-only and keyword only
#you can combine the two argument keys in the same fumnction.

# Any arguments before the / , positional only, and any argument the after the * are keyword only.

def my_function(a,b,/,*,c,d):
    print(a+b+c+d)

my_function(5,6,c=7,d=8)