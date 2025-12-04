x = 2 # Int data type
y = "hello" # String data type

temp ="22.5" 

print(temp) # float data type

first_name = "Rohan"
last_name = "Sakhare"

print(first_name,last_name)

print(x)
print(y)

name = str("hello from str function") # this becomes string data type
count = int(10) # this becomes int data type
pi = float(3.14) # this becomes float data type

print(name,count,pi)

print (type(temp)) # to check the data type of variable
print (type(x))
print (type(y))

x = y = z = "Orange"
print(x)
print(y) # all variables have the same value
print(z)


# Unpacking a list into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# x = "Hello World"	  # str
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None


# Variable Names
myname = 'samarth'
my_name = 'samarth'
_my_name ='samarth'

print (_my_name)

# Variable casing
myName = "samarth" # camelcase

print (myName)

MyNameIs ="sam" #Pascal Case
my_name_is = "samam" # snake case

print (MyNameIs,my_name_is)