n=int(input())
arr=list(map(int,input().split()))
m=int(input())
s=0
c=0
for i in range(0,len(arr)):
    if arr[i]==m:
        c+=1       
if c<=n:
    print(c)
else:
    print("0")