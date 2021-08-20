from string import ascii_lowercase, ascii_uppercase
from random import choice

def pwgen(length, with_digits=True, with_uppercase=True):
    
    rand = choice
    lower = [i for i in ascii_lowercase]
    upper = [j for j in ascii_uppercase]
    digits = list(range(10))
    digits = list(map(str, digits))
    
    chars = lower
    if with_digits:
        chars += digits
    if with_uppercase:
        chars += upper
    
    n = 0
    while n == 0:
        password = ""
        for i in range(length):
            password += rand(chars)           
        
        check_lower = any(i in lower for i in password)     # FAJNA LINIJKA
        check_upper = any(i in upper for i in password)
        check_digits = any(i in digits for i in password)
 
        if check_lower:
            n = 1
        if with_digits:
            if check_digits:
                n *= 1
            else:
                n = 0
        if with_uppercase:
            if check_upper:
                n *= 1
            else:
                n = 0

    return password

print(pwgen(6))