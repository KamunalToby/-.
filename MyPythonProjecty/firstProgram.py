
from tabulate import tabulate

print("Write youre name: ")
name = input()
name2 = input()
print("Write youre gender: ")
gender = input()
gender2 = input()

print("Write youre age: ")
age = input()
age2 = input()

mydata = [
    [name, gender, age],
    [name2, gender2, age2]
]
head = ['Name', 'Gender', 'Age']

print(tabulate(mydata, headers=head, tablefmt="grid"))