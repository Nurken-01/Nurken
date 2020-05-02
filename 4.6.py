def power(a, n):
    if n == 0:
        return 1
    N = power(a * a, n // 2)
    if n % 2:
        N *= a
    return N
a = float(input())
n = float(input())
print(power(a, n))
