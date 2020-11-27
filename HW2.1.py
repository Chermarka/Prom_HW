import sys
import math


a = float(sys.argv[1])
b = float(sys.argv[2])
y = float(sys.argv[3])
vy = (-(a - b) ** 2) / (2 * (y ** 2))
F = (1 / (y * (math.sqrt(2 * math.pi)))) * (math.exp(vy))
print(F)