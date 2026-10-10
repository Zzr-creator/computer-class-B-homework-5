"""n,k=map(int,input().split())
l=list(map(int,input().split()))
left=0;right=min(left+k-1,len(l)-1)
sigma=0
from collections import deque
while right<n:
    crime=[]
    crime=deque(crime)
    current=set(l[left:right+1])
    if -1 not in current:
        left+=1
        right+=1
        continue#全是正数就继续

    else:
        negative=l[left:right+1].count(-1)
        for i in range(left,right+1):
            if l[i]<0:
                crime.append(i)#存储负数的位置

        pointer=left
        while negative>0 and pointer<=right :
            if l[pointer]>0 and negative>0 and len(crime)>0:
                if crime[0]>pointer:
                    l[pointer]-=1
                    l[crime[0]]=0
                    crime.popleft()
                    negative-=1#从左到右，依次让最老的警察处理犯罪，让最久远的犯罪被最先处理
                else:
                    pointer+=1
                    if negative>0:
                        crime.popleft()
            elif l[pointer]<=0:
                pointer+=1

        left+=1
        right+=1
        #print(l)
sigma=l.count(-1)
print(sigma)"""#错误！
n,k=map(int,input().split())
l=list(map(int,input().split()))#按分钟模拟，按队列保留警员批次
police=[]
sigma=0
from collections import deque
police=deque(police)
for i in range(len(l)):

    b=0
    
    if l[i]>0:
        police.append([l[i],i+k-1])
    if len(police)==0 and l[i]<0:
            sigma-=l[i]
            continue
    if i>police[0][1]:
        police.popleft()
    if len(police)==0 and l[i]<0:
            sigma-=l[i]
            continue
    
    if l[i]<0:
            police[0][0]-=1
            if police[0][0]==0:
                 police.popleft()
print(sigma)
            

