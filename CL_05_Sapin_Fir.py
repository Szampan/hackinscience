import sys
print(int(sys.argv[1]))

def fir(segments=3):
    if segments == 0:
        return
    
    last_width = 1    
    tree = []    
    for segment in range(segments):        
        for i in range(4+segment):  
            tree.append(((2*i+1)+(last_width - round(.5+segment)-1) )*"*")
            if i == (3+segment):
                last_width = 2*i + 1 + (last_width - round(.5+segment) - 1)   
    for i in range(segments):
        tree.append((round(0.5+segment)+1)*"|") 

    full_width = len(max(tree, key=len))    
    for i in tree:
        print(i.center(full_width))
    

fir(int(sys.argv[1]))