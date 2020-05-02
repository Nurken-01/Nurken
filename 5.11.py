n = input()
line = list(map(int, input().strip().split()))
x = int(input().strip())
res = line[0]
for i in line:
    if abs(res - x) > abs(i - x):
        res = i
print(res)
