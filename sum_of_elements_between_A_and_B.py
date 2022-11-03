n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        l.append(arr[i])
d=len(l)
s=0
for i in range(d):
    s+=l[i]
print(s)    