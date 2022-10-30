n=int(input())
arr=list(map(int,input().split()))
s=0
a=0
for i in range(1,n+1):
    if arr[n-i]==1:
        s=s+2**(a)
    a+=1
print(s)    