#Factorial using function

def factorial(n):
    if(n >= 1):
        return n*factorial(n-1)
    else:
        return 1

def main():
    number = input("Enter Factorial Number:")
    print("The factorial is {0}".format(factorial(int(number))))

if __name__ == "__main__":
    main()

