line = [int(i) for i in input().split()]
Min = 1000
for i in range(1, len(line)):
    s = int(line[i])
    if (s < Min) and (s > 0):
        Min = s
print(Min)
