a = [int(i) for i in input().split()]
dig = a[0]
index = 0
for i, x in enumerate(a):
    if x >= dig:
        index = i
        dig = x
print(dig, index)
