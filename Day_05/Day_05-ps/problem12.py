# in folwlwing progam what happens when the user enter same name twice ?

dict = {}

name = input("Enter you name: ")
lang = input(("Enter your lang: "))

dict.update({name:lang})
name = input("Enter your name")
lang = input("Enter your lang")

dict.update({name:lang})
name = input("Enter you name: ")
lang = input(("Enter your lang: " ))

dict.update({name:lang})
name = input("Enter you name: ")
lang = input(("Enter your lang: "))

dict.update({name:lang})

print(dict) 
# {'sur ': 'golang', 'gap ': 'java ', 'lorvord': 'python '}


# it will print the updated new value for the user