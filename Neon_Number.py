a=int(input())
s=0
p=a*a
while p:
    r=p%10
    s+=r
    p=p//10
if s==a:
    print("Neon Number")
else:
    print("Not Neon Number")