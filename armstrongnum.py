#Armstrong number check

def armstrong(n):
    number = n
    sum = 0
    order = len(str(n))
    while(n!=0):
        temp=int(n%10)
        n=int(n/10)
        sum =sum + pow(temp,order)
    if(number == sum):
        return print(f"This {number} is an Armstrong number")
    else:
        return print(f"This {number} is not an Armstrong number")

def main():
    number = input("Check for Armstrong Number:")
    armstrong(int(number))

if __name__ == "__main__":
    main()
