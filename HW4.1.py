import sys

STR = str(sys.argv[1]).lower().replace(' ','')
print(STR)
polindrom = True

for i in range(int(len(STR)/2)):
    if STR[i] != STR[len(STR) - 1 - i]:
        polindrom = False

if polindrom:
    print("YES")
else:
    print("NO")