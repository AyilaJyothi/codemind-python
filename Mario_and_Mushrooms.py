n=int(input())
if(n%3==0):
    print("NORMAL")
elif((n-1)%3==0):
    print("HUGE")
else:
    print("SMALL")