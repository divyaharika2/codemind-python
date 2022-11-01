n=int(input())
arr=list(map(int,input().split()))
p=set()
s=0
for i in range(n):
    if arr[i]%2==0:
        p.add(arr[i])
for i in p:
    s+=1
print(s)    
    