n = int(input("Enter the number of terms in the Fibonacci series: "))  # Input from user
a, b = 0, 1  # Initialize the first two terms

print("Fibonacci series:")
for i in range(n):
    print(a)
    c = a + b  # Next term is the sum of the previous two terms
    a = b  # Update a to the next term
    b = c  # Update b to the next term

# output Example:
# If user inputs 7, the output will be:
# Fibonacci series:
# 0
# 1
# 1
# 2
# 3
# 5
# 8 