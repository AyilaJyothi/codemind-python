a,x,y,z=map(int,input().split())
if(a==x or a==y or a==z or a==(x+y) or a==(y+z) or a==(x+z) or a==(x+y+z)):
    print("YES")
else:
    print("NO")