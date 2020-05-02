a = input()
a = a[:a.find('h')] + a[a.rfind('h') + 1:]
print(a)
