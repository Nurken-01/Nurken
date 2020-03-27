N = int(input())
a = 0
b = 1
while b <= N:
    a = a + 1/(b ** 2)
    b = b + 1
print (a)
