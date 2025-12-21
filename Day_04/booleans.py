# print(10 > 9)  #True
# print(11<3)   # false
# print(10 == 9)   # False

# # String Casting
# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")



# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(type(a), type(b))

# if a > b:
#     print("a is grater than b")
# elif a < b:
#     print("a is less than b")
# else:
#     print ("a is equal to b")

age =int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote.")
elif age < 0:
    print("You are not eligible to vote. your age is 0.")
elif age > 120:
    print("Invalid age enterd. age can't be greater than 120.")
elif age == 0:
    print("you are not eligible to vote. your age is zero.")
elif age < 18:
    print ("you are not eligible to vote. your age is less than 10. your age is ", age)
elif age !=0 and age < 18:
    print("you are not eligible to vote. your age is ", age) 
else:
    print("You are not eligible to vote.")
