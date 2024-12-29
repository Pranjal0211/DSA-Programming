def palindrome(n):
    # n = int(input("enter number: "))
    ld=0
    rev = 0 
    dup=n

    while n>0 :
        ld = n % 10
        rev = (rev * 10)+ ld
        n = n//10

    return dup == rev

def main():
    num = 4554

    if palindrome(num):
        print(num, "is palindrome")
    else:
        print(num, "is not palindrome")

if __name__ == "__main__":
    main()        