n=int(input())
c=0
b=[]
for i in range(0,n):
    a=int(input())
    b.append(a)
x=int(input())
for i in b:
    if(i<=x):
        c=c+1
    else:
        c=c+2
print(c)