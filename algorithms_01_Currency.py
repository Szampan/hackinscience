def how_to_pay(amount, currency):
    currency.sort(reverse = True)
    toPay = {500: 0, 200: 0}
    tmp = amount
    for i in currency:
        while tmp >= i:        
            tmp -= i
            if i in toPay:
                toPay[i] += 1
            else: 
                toPay[i] = 1
    
    #print(toPay)
    return toPay