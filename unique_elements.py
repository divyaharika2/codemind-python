n=int(input())
arr=list(map(int,input().split()))
a=[]
for i in range(n):
    s=0
    for j in range(i+1):
        if arr[i]==arr[j]:
            s+=1    
            
    if s==1:
        a.append(arr[i])
print(*a)        
    