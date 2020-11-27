import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

string = "Everybody sing a song:"

for i in range(y):
    string += " "
    for k in range(x):
        if k != x-1:
            string += "la-"
        else:
            string += "la"

if z == 1:
    string += "!"
elif z == 0:
    string += "."
else:
    print("Incorect Z")

print(string)