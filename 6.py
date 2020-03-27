P = int(input())
X = int(input())
Y = int(input())

if Y < 10:
    n = Y / 10
elif Y > 99:
    n = Y / 1000
else:
    n = Y / 100

numA = X + n
m = numA / 100
percent = m * P
numB = numA + percent

import math

numC = math.floor(numB)
numD = numB - numC

if numD > 10:
    number = numD * 10
elif numD < 10:
    number = numD * 100
elif numD < 1:
    numberA = numD * 1000
numberA = round(number)

print(numC, numberA)