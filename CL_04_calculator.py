import sys

if len(sys.argv) != 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
    sys.exit(1)
    

try:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        output = a + b
    elif op == "-":
        output = a - b
    elif op == "*":
        output = a * b
    elif op == "/":
        output = a / b
    elif op == "%":
        output = a % b
    elif op == "^":
        output = a ** b
    
    print(output)

    
except:
    print("input error")




