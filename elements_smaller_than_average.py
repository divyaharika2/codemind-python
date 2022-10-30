n=int(input())
arr=list(map(int,input().split()))
a=int(sum(arr)/len(arr))+1
s=0
for i in range(n):
    if arr[i]<a:
        s+=1
print(s)        