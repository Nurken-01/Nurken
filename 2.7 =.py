a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print('3')
    else:
        print('2')
elif b == c:
    if c == a:
        print('3')
    else:
        print('2')
elif c == a:
    if c == b:
        print('3')
    else:
        print('2')
else:
    print('0')
