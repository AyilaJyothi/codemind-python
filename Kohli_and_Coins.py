n=int(input())
a=0
b=0
b=n//10
n-=b*10
a=n//5
n-=a*5
if n==0:
    c=a+b
    print(c)
else:
    print(-1)