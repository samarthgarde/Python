# Program: Detect spaces in a string

name = "Hello DevOps is a really good field"

# find Double space

double_space_index = name.find(" ")

if double_space_index != -1:
    print(f"Double Space found at index {double_space_index}")

else:
    print("No Double space found")