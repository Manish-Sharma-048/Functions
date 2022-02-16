'''
Write the function to calculate the factorial of a entered number.
'''

num = int(input("Enter number: "))
prod = 1
def fact():
    prod = 1
    for i in range(1,num+1):
        prod = prod * i
    return prod

print("The factorial of", num, "is: ", fact())
