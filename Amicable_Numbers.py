n=int(input())
m=int(input())
b=0
c=0
for i in range(1,n):
    if n%i==0:
        b+=i
for a in range(1,m):        
    if m%a==0:
        c+=a
if (n==c and m==b):
    print("Amicable")
else:
    print("Not Amicable")
        