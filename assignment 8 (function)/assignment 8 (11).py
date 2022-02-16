'''
Write a function that takes numbers entered through keyboard and return the sum of digits of entered numbers.
'''

num = int(input("Enter number: "))
n = num
a = []
b = 0

def tot(n):
    c = 0
    for i in range(len(str(n))):
        b = n%10
        a.append(b)
        n = n//10

    for i in range(len(a)):
        c = a[i] + c

    return c

print("The sum of digits:",num,"is:",tot(n))
