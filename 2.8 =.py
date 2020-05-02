d = int(input())
e = int(input())
a = int(input())
b = int(input())
c = int(input())

if d <= b and e <= c:
    print("YES")
elif d <= c and e <= b:
    print("YES")
elif a <= b and e <= c:
    print("YES")
elif a <= c and e <= b:
    print("YES")
elif d <= e and a <= c:
    print("YES")
elif d <= c and a <= e:
    print("YES")
else:
    print("NO")
