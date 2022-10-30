n=int(input())
arr=list(map(int,input().split()))
s=0
a=0
for i in range(0,n):
    if arr[i]==0:
        s+=1
    elif arr[i]==1:
        a+=1
p=s+a
if n==p:
    print("True")
else:
    print("False")
       