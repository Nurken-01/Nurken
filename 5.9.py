line = [int(i) for i in input().split()]
for i in range(1, len(line)):
    if line[i] > line[i - 1]:
        print(line[i])
