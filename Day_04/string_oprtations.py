print("Hello")   #single quotation 
print('Hello')    #double quotation

print("He is called 'Johnny'")   #Quotes Inside Quotes

a = "Hello"
print(a)


a = "Hello,World!"       # Strings are Arrays
print(a[1])

b = "Hello, World!"      #Slice From the Start
print(b[:5])


b = "Hello, World!"    # Slicing position 2 to position 5
print(b[2:5])


# String Slicing

text = "Programming"

print(text[0:6])   # Progra
print(text[3:7])   # gram
print(text[:4])    # Prog
print(text[4:])    # ramming


# String Length

msg = "Hello World"
name = 'samarthgarde007@gmail.com'
print(len(msg))   # 11
print(len(name))  #25

# Important String Methods

name = "Samarth Garde"

print(name.lower())     # samarth garde
print(name.upper())     # SAMARTH GARDE
print(name.title())     # Samarth Garde
print(name.capitalize())# Samarth garde

# email = 'samarthgarde007@gmail.com'

# print(email.lower())     
# print(email.upper())     
# print(email.title())    
# print(email.capitalize())


# remove spaces

text = "  hello python  "

print(text.strip())   # hello python
print(text.lstrip())  # left space remove
print(text.rstrip())  # right space remove


# replace() method

msg = "I love cricket"

print(msg.replace("cricket", "hollyball"))
# I love hollyball

# find() method

msg = "Python Programming"

print(msg.find("Python"))  # 0
print(msg.find("Java"))    # -1


# String Concatenation

first = "Samarth"
last = "Garde"

print(first + " " + last)


# f-string

name = "Samarth"
age = 22

print(f"My name is {name} and my age is {age}")
