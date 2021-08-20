import sys


try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)
except:
    print("usage: python3 solution.py OP1 OP2")