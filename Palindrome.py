def palindrome(n):
    s=0
    m=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if m==s:
        print("True") 
    else:
        print("False")
n=int(input())
palindrome(n)