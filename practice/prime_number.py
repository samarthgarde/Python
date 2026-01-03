num = int(input("Enter a number: "))    # Input from user

if num < 1:   # Check for numbers less than 1
    print(f"{num} is not a prime number.") # Negative numbers and 0, 1 are not prime
else:
    for i in range(2, num): # Check for factors from 2 to num-1
        if (num % i) == 0:    # If num is divisible by i
            print(f"{num} is not a prime number.")    # Found a factor, so not prime
            break # Exit the loop if a factor is found
    else:
        print(f"{num} is a prime number.")  # No factors found, so it's prime


# output Example:
# If user inputs 7, the output will be:
# 7 is a prime number.
# If user inputs 10, the output will be:
# 10 is not a prime number.