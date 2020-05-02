n = int(input())
x = n
while n != 0:
    n = int(input())
    if n == 0:
        break
    if n > x:
        x = n
print(x)
