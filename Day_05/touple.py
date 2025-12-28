my_tuple = (1,2,3,4,5,6)  # we will use the perentesis to define the tuple in python
print(f"This is for tuple {my_tuple}")

mix_tuple = (10,"hello",20,"True")
print(f"this is for  {mix_tuple}")
print(mix_tuple[-1])      # negative indexing
print(mix_tuple[2:5])     # Range of Indexes


my_tuple1 = (1, 22, 3, 2, 4)
print(my_tuple1.count(1))      # count method
print(my_tuple1.index(3))       # index method

print(type(my_tuple))         # type()constructor


# Loop Through a Tuple
thistuple = ("apple","banana","cheery")
for x in thistuple:
    print(x)

# Loop Through the Index Numbers

thistuple1 = ("samarth","omkar","gurunath","someshwar")    # ()len, ()range fuction for using For loop
for i in range(len(thistuple1)):
    print(i)
    
thistuple2 = ("lokesh","omkar","ram","gopi")    # This is for While loop tuple using len() function while index number
i = 0
while i < len(thistuple2):
    print(thistuple2[2])
    i=i+1


# This is for the joining Tuples

join_tuple1 = ("akash","om","kartik","vish")
join_tuple2 = ("loskesh","kkaak","jjaj","qjqjq")

join_tuple3 = join_tuple1 + join_tuple2
print(join_tuple3)
