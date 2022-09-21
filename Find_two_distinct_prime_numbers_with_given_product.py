n=int(input())
s=1
for i in range(2,n):
    if n%i==0:
        print(i,end=" ")
        s*=i
if  s==n:
    pass
else:
    print("-1")