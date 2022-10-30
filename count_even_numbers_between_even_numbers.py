n=int(input())
arr=list(map(int,input().split()))
x=0
for i in range(0,n-2):
    if arr[i]%2==0 and arr[i+1]%2==0 and arr[i+2]%2==0:
        x+=1
print(x)        