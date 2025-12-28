# Dictionaries are written with curly brackets, and have keys and values:

my_dict = {
    "value1":"D-mart",
    "value2":"Zomato",
    "year":2025,
    "colors": ["red","green","white"]
}
my_dict["year"]=2030          # Change values
my_dict.update({"year":2000})  # This is for update the key
my_dict.pop("value2")       # this methods is to remove item like "value2" from a dictionary
my_dict.clear()         # clear all the dictionary

print(my_dict)

print(my_dict)               # outpust Shows the key value pairs
print(my_dict["value1"])       # give the o/p is D-mart
print(len(my_dict))          # Dictionary length
print(type(my_dict))          # Type of dictionary

# The dict() Constructor
my_dict1 = dict(name="samarth",last_name="Garde",age=22,country="India")
print(my_dict1)

# Looping through keys
for dict in my_dict1:
    print(dict) 

for dict in my_dict:
    print(dict) 

# Looping through values
for dict in my_dict.values():          # values() function using the loop
    print(dict)