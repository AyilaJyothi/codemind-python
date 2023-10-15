n=int(input())
h=n//3600
a=n-(h*3600)
m=a//60
s=a%60
print("H:M:S-%d:%d:%d"%(h,m,s))