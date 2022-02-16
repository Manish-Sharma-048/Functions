'''
Write the function to find out whether entered number is prime or not.
'''

num = int(input("Enter number: "))
count = 0

def prime():
    count = 1
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                count = count + 1
    return count

count = prime()

def f_val(count):
    if count > 1:
        print("It is not a prime number")
    else:
        print("It is a prime number.")

f_val(count)
