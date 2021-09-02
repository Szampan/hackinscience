import math

def is_prime(n):
    if n == 1 or n == 0:
        return False       
    m = int(math.sqrt(n))    
    for i in range(2, m+1): 
        if (n % i) == 0:
            return False
    return True

if __name__ == "__main__":
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(271)
    assert not is_prime(272)