# Definition:
# n! = n × (n-1) × (n-2) × ... × 1

# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 4! = 4 × 3 × 2 × 1 = 24
# 3! = 3 × 2 × 1 = 6
# 0! = 1 (by definition)

num = int(input("Enter a number: "))  # Input from user
factorial = 1  # Initialize factorial variable

for i in range(1, num + 1):  # Loop from 1 to num
    factorial *= i  # Multiply factorial by the current number

    print(f"Factorial is:", factorial)  # Print the factorial value at each step

# output Example:
# If user inputs 5, the output will be:
# Factorial is: 1
# Factorial is: 2
# Factorial is: 6
# Factorial is: 24
# Factorial is: 120

