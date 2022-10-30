n=int(input())
arr=list(map(int,input().split()))
x=0
if n==0:
    print("0")
else:
    for i in range(n-2):
        if arr[i]%2==0 and arr[i+2]%2!=0:
            x+=1
        elif arr[i]%2!=0 and arr[i+2]%2==0:
            x+=1
print(x)            
            