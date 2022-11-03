def prime(n):
    if n==0 or n==1:
        return False
    else:
        s=int(n**0.5)
        for i in range(2,s+1):
            if n%i==0:
                return False
    return True
c=0    
m=int(input())
n=int(input())
for i in range(m,n+1):
    if prime(i):
        print(i)
                