import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("triangle")
else:
    print("not triangle")