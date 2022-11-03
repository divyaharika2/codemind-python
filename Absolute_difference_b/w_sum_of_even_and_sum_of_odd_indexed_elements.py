n=int(input())
arr=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    if i%2==0:
        s+=arr[i]
    if i%2!=0:
        c+=arr[i]
if s>c:
    print(s-c)
else:
    print(c-s)