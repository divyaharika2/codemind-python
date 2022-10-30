n=int(input())
a=list(map(int,input().split()))
s=0
p=int(sum(a)/len(a))
for i in range(n):
    if a[i]>=p:
        s+=1
print(s)        