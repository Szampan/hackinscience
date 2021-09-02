def perfect_shuffle(deck):
    a = []
    b = []
    index = 0
            
    #print(deck)
    for i in deck:
        # print(index, i)        
        if index > (len(deck)/2 - 1):
            b.append(i)
        else:
            a.append(i)
        index += 1        
        
    tmp = sum(zip(a,b), ())
    return list(tmp)
    

if __name__ == "__main__":
    assert perfect_shuffle([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]