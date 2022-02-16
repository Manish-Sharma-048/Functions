'''
Write the function to print the entered number in reverse order.
'''

num = input("Enter number: ")

def revnum():
    rev = num[::-1]
    print(rev)

revnum()
