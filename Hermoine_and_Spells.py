a,b,c=map(int,input().split())
if((a+b)>(a+c) and (a+b)>(b+c)):
    print(a+b)
elif((b+c)>(a+b) and (b+c)>(a+c)):
    print(b+c)
else:
    print(a+c)