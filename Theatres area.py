a = int(input())
b = int(input())
c = int(input())
if a%c == 0 and b%c == 0:
    print (a * b/c**2)
elif (a%c == 0): 
    print(a/c)*(b//c+1)
elif (b%c == 0): 
    print(a/c+1)*(b/c)
else:
    print((a//c+1)*(b//c+1))
    
