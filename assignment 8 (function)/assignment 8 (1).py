'''
Write the function to find that entered number even or odd.
'''

num = int(input("Enter number: "))

def eve_odd():
    if num%2 == 0:
        print("The entered number is an even number.")
    else:
        print("The entered number is an odd number.")

eve_odd()
