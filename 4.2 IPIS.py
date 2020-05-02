def IsPointInSquare(x, y):
    n = -1 <= x <= 1 and -1 <= y <= 1
    return n
x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
