# Reverse a Number

num = int(input("Enter a number: "))
rev = 0  # Initialize reversed number

while num > 0:         # Loop to reverse the number
    digit = num % 10     # Get the last digit
    rev = rev * 10 + digit
    num = num // 10
print(f"Reversed Number: {rev}")

# Example:
# input --- 1234
# output --- Reversed number: 4321

# Reverse a String

word = input("Enter a word: ")
reversed_word = word[::-1]  # Reverse the string using slicing
print(f"Reversed String: {reversed_word}")

# output Example:
# If user inputs hello, the output will be:
# Reversed String: olleh
