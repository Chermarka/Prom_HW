import sys

STR = str(sys.argv[1])
new_STR = ""
list_of_words = list(STR.split(" "))

for word in reversed(list_of_words):
    new_STR += word + " "

print(new_STR)