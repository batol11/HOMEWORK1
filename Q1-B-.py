#Question1 -B-
def factorial (n):
    if n== 0:
        return 1
    else:
        return n * factorial(n-1)
    num = int(input("Enter a number"))
    if num < 0:
        print("factorial is'nt defined for negative numbers")
    elif num==o:
        print("the factorial is 1")
    else:
        result = factorial(num)
        print (f"the factorial of {num} is {result}")
