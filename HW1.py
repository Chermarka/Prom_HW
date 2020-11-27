import sys
import math


a = float(sys.argv[1])
b = float(sys.argv[2])
if a >= 0 and b >= 1:
    stepn = (2 * a) / b
    rez = (math.sqrt(a * b) / ((math.e ** a) * b)) + (a * (math.e ** stepn))
    print(rez)
else:
    print("invalid data")