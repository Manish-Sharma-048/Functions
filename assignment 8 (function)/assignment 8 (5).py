'''
Write the function to print the Fibonacci series. The number of terms for Fibonacci series will be entered through keyboard.
'''

num = int(input("Enter number: "))

def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series, end = ' ')
        num1 = num2
        num2 = series
        series = num1+num2

fibonacci(num)
