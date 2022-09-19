n=int(input())
s=0
t=n
while n>0:
    i=1
    fact=1
    r=n%10
    while i<=r:
        fact=fact*i
        i+=1
    s+=fact
    n=n//10
if s==t:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")