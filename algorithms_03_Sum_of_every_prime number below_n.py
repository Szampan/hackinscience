import math

def is_prime(n):
    if n == 1 or n == 0:
        return False       
    m = int(math.sqrt(n))
    
    for i in range(2, m+1): 
        if (n % i) == 0:
            return False
    return True    
def sum_primes(num):
    tmp = 0
    for i in range(num):        
        if is_prime(i):
            tmp += i
    return tmp
#    print(tmp)
            
#sum_primes(79)