import math
n = float(input())
if (n - int(n)) < 0.5:
    print(math.floor(n))
else:
    print(math.ceil(n))
