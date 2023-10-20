a,b,c,d,e=map(int,input().split())
f=((a+b+c+d+e)/500)*100
if(f>=90):
    print("Grade A")
elif(f>=80 and f<90):
    print("Grade B")
elif(f>=70 and f<80):
    print("Grade C")
elif(f>=60 and f<70):
    print("Grade D")
elif(f>=40 and f<60):
    print("Grade E")
elif(f<40):
    print("Grade F")