import time
start_time = time.time()

def changes(amount, coins):    
    amount = tuple([amount])
    coins = sorted(list(coins), reverse=True)

    possibilities = set()
    knowledge = {}

    def divide(sequence):
        print('Divide ', sequence)
        new_sequences = set()
        tmp_coins = [i for i in coins if i < sequence[0]]
        for n in range(len(sequence)):          #lepiej rozkminić ten algorytm dzielący...            
            
            if sequence[n] in knowledge and sequence[n] != 1:          # o tutaj można zrobić list comprehension
                
                # print("SŁOWNIK: DLA KLUCZA ", sequence[n], "WARTOŚĆ WYNOSI:", tuple(knowledge[sequence[n]]))
                # print('TEST ', sequence[0:n], tuple(knowledge[sequence[n]]), sequence[n+1:])
           
                # new_sequences = set(
                #     tuple(sorted(sequence[0:n] + value + sequence[n+1:], reverse=True)) 
                #     for value in knowledge[sequence[n]]  if tuple(sorted(sequence[0:n] + value + sequence[n+1:], reverse=True)) not in possibilities
                #     )
                # new_sequences.difference(possibilities)

                # print('NEW SEQUENCES: ', new_sequences)
                for value in knowledge[sequence[n]]:
                    new_seq = tuple(sorted(sequence[0:n] + value + sequence[n+1:], reverse=True))                                    
                    if new_seq not in possibilities: 
                        new_sequences.add(new_seq)

            elif sequence[n] != 1: 
                knowledge[sequence[n]] = set()
                for idx in range(len(tmp_coins)):
                    divided = []
                    # idx = tmp_coins.index(coin)
                    c = 0
                    while sum(divided) < sequence[n]:
                        if sum(divided) + tmp_coins[idx+c] <= sequence[n]:
                            divided.append(tmp_coins[idx+c])
                        else:
                            c += 1
                    
                    new_seq = tuple(sorted(sequence[0:n] + tuple(divided) + sequence[n+1:], reverse=True)) # tu jest za wolno. to powinna być krotka od początku
                                                                                                            # a może lepiej skopiować new_seq = [*sequence] apozniej pozmienic wartość?

                    knowledge[sequence[n]].add(tuple(divided))
                    
                    
                    if new_seq not in possibilities: # and new_seq not in new_sequences: 
                        new_sequences.add(new_seq)
                print('KNOWLEDGE updated: ', knowledge)

    
            
        print('append "new_sequences" to "possibilities": ', new_sequences)


        possibilities.update(new_sequences)
        # map()?
        for sqc in new_sequences:
            divide(sqc)


    if amount[0] in coins:
        possibilities.update(amount)
        print('Run divide() on the first (and only) element of "possibilities"')     
        divide(amount)   
    else:        
        print('Run divide() on [amount]')
        divide(amount)

    print()
    # print('Possibilities: ', possibilities)

    return len(possibilities)




print()
# print(changes(90, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(62, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
# print(changes(20, (1, 2, 5, 10, 20, 50, 100, 200, 500)))

print(changes(6, (1, 2, 3, 4, 5)))

print(f'--- {round(time.time() - start_time, 5)} seconds ---')



