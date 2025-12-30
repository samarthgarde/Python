#  write an prgram to find out the user enter numebr avrage

n = int(input("Enter how many numbers: "))

sum = 0

for i in range(n):
    num = int(input("Enter number: "))
    sum = sum + num

average = sum / n
print("Average is:", average)
