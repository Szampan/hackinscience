import math


def print_pascal_triangle(height):
    triangle = []
    
    for i in range(height):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(sum(triangle[i-1][j-1:j+1]))

        triangle.append(row)

    max_length= len(str(max(triangle[height-1])))

    def spaces(num):             
        length = max_length - len(str(num))
        if max_length % 2 == 0:
            return length + 1
        else: 
            return length

    print('max length: ', max_length)
    
    def before(row): 
        return int(math.ceil((max_length+1)/2) * (height - row -1))     
    
    for k in triangle:
        print(before(triangle.index(k)) * ' ', end='')  
        for m in k:
            print(m, spaces(m)*' ', end='')
        print()

    #
print_pascal_triangle(14)
