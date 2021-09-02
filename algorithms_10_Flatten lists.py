def flatten(a_list):
    numbers = []
    
    def check(obj):    
        if isinstance(obj, list):
            for i in obj:
                obj = i
                check(obj)
        else:        
            numbers.append(obj)
        
    check(a_list)
    return numbers

flatten([1, [2, 3], 4, 5])


if __name__ == "__main__":
    print(flatten([1]))
    print(flatten([1, 2, 3]))
    print(flatten([1, [2, 3], 4, 5]))
    print(flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))