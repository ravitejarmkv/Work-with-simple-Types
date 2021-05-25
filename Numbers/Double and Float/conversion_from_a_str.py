from locale import *
strPi = "3.14"
piFloat = float(strPi)

strExp = "2.71828"
exp = atof(strExp)

strHalf = "0,5"
half = atof(strHalf.replace(",", "."))

print(piFloat)
print(exp)
print(half)