a = int(input())
b = int(input())
c = int(input())
x = (a + b + c) / 2
Answer = (x * (x - a) * (x - b) * (x - c)) ** 0.5
print (Answer)