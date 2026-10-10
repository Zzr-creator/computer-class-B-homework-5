from collections import deque
n,c=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
l=deque(l)
sigma=0
while len(l)>0:
    if c-l[0]>=l[-1] and len(l)>1:
        sigma+=1
        l.popleft()
        l.pop()
    else:
        sigma+=1
        l.popleft()
print(sigma)


n,c=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
left=0;right=n-1
sigma=0
while left<=right:
    if c-l[left]>=l[right]:
        left+=1
        right-=1
        sigma+=1
    else:
        left+=1
        sigma+=1
print(sigma)

