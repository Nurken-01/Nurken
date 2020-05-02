n = input()
count = len(n) - len(n.replace('f', ''))
if count == 0:
    pass
elif count == 1:
    print(n.index('f'))
else:
    print(n.index('f'), n.rindex('f'))
