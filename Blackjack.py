a,b=map(int,input().split())
for i in range(1,11):
    c=21-a-b
    if(c<=10):
        print(c)
        break
    else:
        print("-1")
        break