a=int(input())
s=0
f=1
while a:
    r=a%10
    s+=r
    f*=r
    a=a//10
if s==f:
    print("Spy Number")
else:
    print("Not Spy Number")
    