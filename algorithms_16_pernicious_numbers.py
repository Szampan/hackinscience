import math

def is_prime(n):
    if n == 1 or n == 0:
        return False
       
    m = int(math.sqrt(n))
    
    for i in range(2, m+1): 
        if (n % i) == 0:
            return False
    return True

for i in range(222281, 222381):
    num = str(bin(i))[2:]
    digits_sum = sum(int(digit) for digit in num)
    
    if is_prime(digits_sum):
        print(i)


# Można zmienić algorytm - wystarczy, że liczba jedynek w numerze binarnym jest liczbą pierwszą
