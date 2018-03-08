def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num-1) * num

def main():
    number = int(input("Enter a nonnegative integer: "))
    fact = factorial(number)
    print("The factorial of", number, "is", fact)
        
main()
