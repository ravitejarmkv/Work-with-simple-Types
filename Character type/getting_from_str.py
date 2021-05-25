str_variable = "ABC"
charA = str_variable[0]
# charA is "A"

charB = str_variable[1]
# charB is "B"

charC = str_variable[2]
#charC is "C"

charList = ""
for i in str_variable:
    charList += (i + ": ")
# charList is "A: B: C:"

print(charA)
print(charB)
print(charC)
print(charList)