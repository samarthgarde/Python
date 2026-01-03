# Examples of Palindromes:
# Number: 121, 2112, 12321, etc.
# String: madam, racecar, level, etc.


# Palindrome Number Program

num = int(input("Enter a number: "))

temp = num       # Store the original number 
rev = 0          # Initialize reversed number

while num > 0:         # Loop to reverse the number
    digit = num % 10     # Get the last digit
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:                # Check if original number and reversed number are the same
    print(f"{temp} is a palindrome.") 
else:
    print(f"{temp} is not a palindrome.")




# Palindrome String Program

word= input("Enter a word: ")

if word == word[::-1]:   # Check if the string is the same forwards and backwards
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# output Example:
# If user inputs 121, the output will be:
# 121 is a palindrome.
# If user inputs madam, the output will be:
# madam is a palindrome.