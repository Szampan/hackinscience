import time
start_time = time.time()

def changes(amount, coins):    

    coins = sorted(coins, reverse=True)
    possibilities = []
    # possibilities = {}
    

    def divide(sequence):
        print('Divide ', sequence)
        # new_sequences = set()
        new_sequences = []
        tmp_coins = [i for i in coins if i < sequence[0]]
        for n in range(len(sequence)):
            for coin in tmp_coins:
                  
                # print(coin)
                # new_seq = sequence[:]
                new_seq = [*sequence]
                divided = []            # może tego można teraz nie deklarować, tylko później stworzyć??

                gen = (i for i in tmp_coins if i <= coin)
                for x in gen:
                    while sum(divided) < sequence[n]:                        
                            if x + sum(divided) <= sequence[n]:
                                divided.append(x)
                            else:
                                break

                # for i in tmp_coins:
                #     if i <= coin:
                #         while sum(divided) < sequence[n]:                        
                #             if i + sum(divided) <= sequence[n]:
                #                 divided.append(i)
                #             else:
                #                 break

                new_seq[n:n+1] = divided
                
                # print('new_seq: ', new_seq)
                new_seq.sort(reverse = True)
                # if new_seq not in possibilities:
                #     new_sequences.update(new_seq)
                
                if new_seq not in possibilities and new_seq not in new_sequences: 
                    new_sequences.append(new_seq)
            

        print('append "new_sequences" to "possibilities": ', new_sequences)

        """
        spróbować tak: funkcja(divide) zamiast extendować possibilities, powinna returnować listę: func(AAAA) -> return [AAAA, AA AA, A A A A]
        """
        possibilities.extend(new_sequences)

        # map(divide, new_sequences)

        for sqc in new_sequences:
            divide(sqc)



    if amount in coins:
        possibilities.append([amount])
        print('Run divide() on the first (and only) element of "possibilities"')     
        divide(possibilities[0])   
    else:
        # possibilities = [divide(amount)]


        print('Run divide() on [amount]')
        divide([amount])

    print()
    print('Possibilities: ', possibilities)

    return len(possibilities)




print()
# print(changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
print(changes(69, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500)))

# print(changes(5, (1, 2, 3, 4, 5, 6)))

print(f'--- {round(time.time() - start_time, 5)} seconds ---')



