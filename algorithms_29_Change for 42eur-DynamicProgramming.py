import time
start_time = time.time()

def changes(amount, coins):   
    tab = []
    for i in range(len(coins)):
        tab.append([])
        for value in range(amount + 1):
            if i == 0:
                if value % coins[i] == 0:                
                    tab[i].append(1)
                else:
                    tab[i].append(0)
            elif coins[i] > value:
                tab[i].append(tab[i-1][value])
            else:
                a = tab[i-1][value] 
                b = tab[i][value - coins[i]]
                tab[i].append(a + b)   
    for i in tab:
        print(i)
    
    return tab[-1][-1]


print()
# print(changes(90, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(62, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(20, (1, 2, 5, 10, 20, 50, 100, 200, 500)))

print(changes(6, (1, 2, 3, 4, 5)))

print(f'--- {round(time.time() - start_time, 5)} seconds ---')



