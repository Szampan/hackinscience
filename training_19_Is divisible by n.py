for i in range(1000+1):
    
    if i % 7 == 0:
        sum = 0
        for j in str(i):
            sum += int(str(j))
        if sum % 3 == 0:
            print(i)
            
  
