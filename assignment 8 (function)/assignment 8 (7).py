'''
Write a function to find entered number through keyboard is whether palindrome or not.
'''

num = input("enter the number: ")
num2 = num[::-1]

def palindrome():
    if num == num2:
        print("This number is a palindrome.")
    else:
        print("This number is not a palindrome.")

palindrome()
