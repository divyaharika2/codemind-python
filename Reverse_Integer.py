n=int(input())
rev=0
m=abs(n)
while m>0:
    r=m%10
    rev=rev*10+r
    m=m//10
if n<0:
    print(-rev)
else:
    print(rev)