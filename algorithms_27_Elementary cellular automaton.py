import sys

def wolfram(rule, current):
    # taking rule number, compute current pattern of 3 cells into new state for center cell
    patterns = ['###', '##.', '#.#', '#..', '.##', '.#.', '..#', '...']
    rule_bin = bin(rule)[2:].zfill(8) # for instance dec110 = bin01101110     
    new = rule_bin[patterns.index(current)]
    if new == '0':
        new = '.'
    else: 
        new = '#'
    return new

def automaton(rule):
    table = []
    table.append(list('.'*79))
    table[0][39] = "#"
    
    for k in range(1,40): 
        tmp = []
        idx = 0
        for m in table[k-1]:            
            center = table[k-1][idx]            
            if idx == 0:
                left = table[k-1][len(table[k-1])-1]  
                right = table[k-1][idx+1]              
            elif idx == (len(table[k-1]) -1 ):  
                left = table[k-1][idx-1]              
                right = table[k-1][0]     
            else:
                left = table[k-1][idx-1]     
                right = table[k-1][idx+1]  
            current_cells = left + center + right            
            idx += 1
            tmp.append(wolfram(rule, current_cells))
        table.append(tmp)
    
    for i in table:        
        for j in i:
            print(j, end='')
        print()
    
if __name__ == '__main__':     
    try:
        automaton(int(sys.argv[1]))
    except:
        print("Give the rule number as a parameter")

    


# print(wolfram(110, '###')) # powinien dać .
# print(wolfram(110, '##.')) # powinien dać #
# print(wolfram(110, '#.#')) # powinien dać #
# print(wolfram(110, '#..')) # powinien dać .



# print(wolfram(110, '111')) # powinien dać 0
# print(wolfram(110, '110')) # powinien dać 1
# print(wolfram(110, '101')) # powinien dać 1
# print(wolfram(110, '100')) # powinien dać 0
# print(wolfram(110, '011')) # powinien dać 1
# print(wolfram(110, '010')) # powinien dać 1
# print(wolfram(110, '001')) # powinien dać 1
# print(wolfram(110, '000')) # powinien dać 0
