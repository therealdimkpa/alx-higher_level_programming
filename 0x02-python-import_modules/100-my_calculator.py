#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    operators = {"+": add, "-": sub, "/": div, "*": mul}

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)

    elif operators.get(sys.argv[2]) is not None:
        action = operators[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], action))
     
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit (1)
