import random

# Snake Water Gun Game
'''
s -> snake
w -> water
g -> gun

'''

youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {'s': 1, 'w': -1, 'g': 0}

resverseDict = {1: 'snake', -1: 'water', 0: 'gun'}

# convert your choice into number
younum = youDict.get(youstr.lower())

# computer  makes a random choice
computer = random.choice([1, -1, 0])

print(f"You chose {resverseDict[younum]}")
print(f"Computer chose {resverseDict[computer]}")

# Game Logic
if younum == computer:
    print("It's a Tie!")
elif (younum == 1 and computer == -1): # snake drinks water
    print("You lose! Computer wins.")
elif (younum == -1 and computer == 0): # water douses gun
    print("You lose! Computer wins.")
elif (younum == 0 and computer == 1): # gun shoots snake
    print("You lose! Computer wins.")
else:
    print("You win!")