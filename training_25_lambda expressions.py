def filtered(iterable, filt):
    return [i for i in iterable if filt(i)]

if __name__ == '__main__':
 
    print(", ".join(map(str, filtered(range(101), lambda x: x % 3 == 0))))
    print(", ".join(map(str, filtered(range(101), lambda y: y % 5 == 0))))
    print(", ".join(map(str, filtered(range(101), lambda z: z % 15 == 0))))