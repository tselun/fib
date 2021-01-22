# calculates fibonacci number using binet's formula

import sys
import math

def fib(n):
    f1 = ((1+math.sqrt(5))/2)**n 
    f2 = ((1-math.sqrt(5))/2)**n
    f = (f1-f2)/math.sqrt(5)
    return int(f)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))


