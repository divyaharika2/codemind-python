n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(n):
    if l[i]<a or l[i]>b:
        k.append(l[i])
if k==[]:
    print("-1")
else:
    print(max(k))
    
    