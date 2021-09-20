## to rozwiązanie nie formatuje trójkąta

def print_pascal_triangle(height):
    content = [1]
    for i in range(height):
        print(' '.join(map(str, content)))
        # print(content, content[1:])
        # print(list(zip(content, content[1:])))
        content = [1] + [a + b for a, b in zip(content, content[1:])] + [1]     # robi listę z sum dwóch kolejnych elementów



'''
# to rozwiązanie formatuje trójkąt

def print_pascal_triangle(h):
    p = [[1]]
    for x in range(h-1):
        p += [[1] + [a+b for a,b in zip(p[-1],p[-1][1:])] + [1]]
    lv = len(str(max(p[-1])))
    lc = len(' '.join(f"{x:<{lv}}" for x in p[-1]))
    for l in p:
        print(' '.join(f"{x:<{lv}}" for x in l).center(lc))
        
'''

print_pascal_triangle(7)