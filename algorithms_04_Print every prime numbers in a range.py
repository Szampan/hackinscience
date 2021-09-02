import math

def is_prime(n):
    if n == 1 or n == 0:
        return False       
    m = int(math.sqrt(n))    
    for i in range(2, m+1): 
        if (n % i) == 0:
            return False
    return True
    
numbers = []
    
for i in range(10000, 10050):
    if is_prime(i):
        numbers.append(str(i))
        
numbers = ', '.join(numbers)

print(numbers)

