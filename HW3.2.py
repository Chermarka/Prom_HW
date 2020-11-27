import sys

n = int(sys.argv[1])

fib0 = 0
fib1 = 1

if n == 0:
    fib1 = 0
else:
    for i in range(n):
        fib_sum = fib0 + fib1
        fib0 = fib1
        fib1 = fib_sum
        
print(fib1)