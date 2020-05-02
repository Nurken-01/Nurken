a = int(input())
if a == 1:
    print(a, 'korova')
elif 2 <= a <= 4:
    print(a, 'korovy')
elif a % 10 == 1:
    if a // 10 == 1:
        print(a, 'korov')
    else:
        print(a, 'korova')
elif 2 <= (a % 10) <= 4:
    if a // 10 == 1:
        print(a, 'korov')
    else:
        print(a, 'korovy')
else:
    print(a, 'korov')
