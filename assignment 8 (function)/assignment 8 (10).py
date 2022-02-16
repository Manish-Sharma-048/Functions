'''
Write a function that takes two numbers entered through keyboard and return greatest of them.
'''

num = int(input("Enter number: "))
num1 = int(input("Enter number: "))

def greatest():
    if num > num1:
        return num
    else:
        return num1

print("The greatest number is:",greatest())
