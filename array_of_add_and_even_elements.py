n=int(input())
arr=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    if arr[i]%2!=0:
        a.append(arr[i])
    elif arr[i]%2==0:
        b.append(arr[i])
c=a+b
print(*c)