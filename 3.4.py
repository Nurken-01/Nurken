a = float(input())
b = round((a - int(a)) * 100)
c = round(a - (b / 100))
print(c, b)
