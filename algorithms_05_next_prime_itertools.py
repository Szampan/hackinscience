from itertools import count
import sys
import math

def is_prime(n):
    if n == 1 or n == 0:
        return False
       
    m = int(math.sqrt(n))
    
    for i in range(2, m+1): 
        if (n % i) == 0:
            return False
    return True

iterator = (count(start = 100000000, step = 1))


for i in iterator:
    if is_prime(i):
        #print(i)
        #break                  #można też print i break
        sys.exit(print(i))    
        

