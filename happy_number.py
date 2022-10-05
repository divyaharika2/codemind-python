n=int(input())
t=n
while t>=10:
    s=0
    while t>0:
        r=t%10
        s=s+(r**2)
        t=t//10
    t=s
if t==1:
    print("True")
else:
    print("False")