'''
Write a function that takes a number entered through keyboard and find whether it is positive or negative.
'''

num = int(input("Enter number: "))

def pos_neg():
    if num > 0:
        print("This is a positive number.")
    elif num == 0:
        print("This is neither negative nor positive")
    else:
        print("This is a negative number.")

pos_neg()
