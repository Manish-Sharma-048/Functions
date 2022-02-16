'''
Write a function that takes two numbers a and b, entered through keyboard and return the value of a to the power b
'''

num = int(input("Enter number: "))
pwr = int(input("Enter number: "))

def tot(a,b):
    sum = a**b
    return sum

print("The sum of",num,"to the power",pwr,"is:",tot(num,pwr))
