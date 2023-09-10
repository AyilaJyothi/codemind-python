n=input()
c=0
m=0
for i in n:
    if i in "aeiou":
        c=c+1
        m=max(c,m)
    else:
        c=0
print(m)
    