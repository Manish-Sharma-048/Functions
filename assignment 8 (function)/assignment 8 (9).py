'''
Write the function to find entered number through keyboard is whether Armstrong or not.
'''

num = int(input("Enter number: "))
n = num

a = []


def arm(n):
    c = 0
    for i in range(len(str(n))):
        b = n%10
        a.append(b)
        n = n//10

    for i in range(len(a)):
        c = c + a[i]**len(a)

    return c

if arm(n) == num:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")
