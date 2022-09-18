n=int(input())
t=n
rev=0
s=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10    
m=rev**2    
while m>0:
    k=m%10
    s=s*10+k
    m=m//10   
if t**2==s:
    print("True")
else:
    print("False")