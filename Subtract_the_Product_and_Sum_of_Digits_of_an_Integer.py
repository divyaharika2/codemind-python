n=int(input())
s=1
t=0
while n>0:
    r=n%10
    s*=r
    t+=r
    n=n//10
print(s-t)    
    