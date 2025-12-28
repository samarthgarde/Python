my_set = {"apple","banana","cheery"}
my_set.add("orange")              # Add an item to a set, using the add() method
tropical = {"pineapple", "mango", "papaya"}
my_set.update(tropical)            # To add items from another set into the current set, use the update() method.
mylist = ["kiwi", "orange"]
my_set.update(mylist)             # Add elements of a list to at set
my_set.remove("banana")           #Remove "banana" by using the remove() method
my_set.discard("banana")          # Remove "banana" by using the discard() method
my_set.copy()            # Copy the my_set
differ = my_set - tropical        # Use - as a shortcut instead of difference()
print(differ)
print(my_set)

set_3 =my_set | tropical          # You can use the | operator instead of the union() method, and you will get the same result
print(set_3)

for x in my_set:                  # You can loop through the set items by using a for loop
  print(x)
print(my_set)          