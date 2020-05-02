a = input()
first = a[:a.find(' ')]
second = a[a.find(' ') + 1:]
print(second + ' ' + first)
