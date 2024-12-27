n = int(input("enter an integer: "))

rev = 0
ld = 0
#rev- reverse ld- last digit

while n > 0:
    ld= n % 10
    rev = (rev * 10) + ld
    n= n // 10

print("reverse: ", rev)
