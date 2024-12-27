def countDigits(n):
    count= 0 
    while n > 0:
        count += 1
        n= n //10
    return count




#driver function
if __name__ == "__main__":
    n= 329823
    print("n", n)
    digits=countDigits(n)
    print("number of digits in n ", digits)