import math

pi = 3.1415

piRound = round(pi, 3)

piTrunc = math.trunc(pi * 1000)/1000.0

piCeil = math.ceil(pi * 100)/100

print(piRound)
print(piTrunc)
print(piCeil)