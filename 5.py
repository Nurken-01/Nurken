N = float(input())

import math

x = math.floor(N)
o = N - x

if o == 0.5:
    c = math.ceil(N)
    print(c)

if o < 0.5:
    a = math.floor(N)
    print(a)

if o > 0.5:
    b = math.ceil(N)
    print(b)