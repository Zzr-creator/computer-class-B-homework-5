n=1000002
primes=[True]*n
primes[0]=False
primes[1]=False
for i in range(n):
    if primes[i]==True:
        for j in range(i*i,n,i):
            primes[j]=False
correct=[]
for i in range(n):
    if primes[i]==True:
        correct.append(i)

s=int(input())
for i in range(s):
    l=int(input())
    left=0;right=n-1
    while left<=right:
        mid=(left+right)//2
        if mid<l:
            left=mid+1
        else:
            right=mid-1
    ans=[]
    while primes[l-correct[left]]==False:
        left-=1
    ans=[left,l-left]
    ans.sort()
    print(*ans)



