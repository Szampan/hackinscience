def fibonacci(n):
    i = 2
        
    if n == 0:
        NUMS = []
    elif n == 1:
        NUMS = [1]    
    elif n >= 2:
        NUMS = [1,1]
                
        while i < n:
            next = NUMS[-2] + NUMS[-1]
            NUMS.append(next)        
            i += 1
    
    return NUMS
