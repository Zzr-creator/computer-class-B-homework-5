### Assignment #5: cs101 Mock Exam 寒露

*Updated: 2026-10-08 (GMT+8)*  
*完成学生：<mark>同学的姓名、院系</mark>*
张择然 工学院



>**说明：**
>
>截止日期：第四到六周作业统一于 10月20日 提交至 Canvas 平台。
>
>内容要求：每个题目包含：**解题思路**（可选）、**源代码**、**Accepted 截图**、**预估耗时**（可选）。
>



## 1. 题目

### E31295:宿舍的空调

http://cs101.openjudge.cn/practice/31295/

思路：



代码

```python
n=int(input())
todo=[]
b=0
for i in range(1,n+1):
    a,b=map(int,input().split())
    todo.append([a,b])
std=todo[0]
for j in range(len(todo)):
    std=[max(std[0],todo[j][0]),min(std[1],todo[j][1])]
    if std[0]<=std[1]:
        pass
    else:
        print(-1)
        b="break"
        break
if b!="break":
    print(std[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E31294:大肥鱼卖白饭

http://cs101.openjudge.cn/practice/31294/

思路：



代码

```python
n=int(input())
l=list(map(int,input().split()))
d={5:0,10:0,20:0}
b=0
for i in range(n):
    if l[i]==5:
        d[5] += 1
        continue

    elif l[i]==10:
        d[10] += 1
        d[5]-=1
    elif l[i]==20:
        d[5]-=1;d[10]-=1
        if d[5]<0 or d[10]<0:
            d[5] += 1
            d[10] += 1
            d[5]-=3

    if d[5]<0 or d[10]<0:
        print("NO")
        b="break"
        break

if b!="break":
    print("YES")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E31293:双十一凑单大作战

http://cs101.openjudge.cn/practice/31293/

思路：



代码

```python
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
sigma=0
for i in range(1,n+1):
    if i%3==0:
        pass
    else:
        sigma+=l[i-1]
print(sigma)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M31297:恒星共振裂变

http://cs101.openjudge.cn/practice/31297/

思路：



代码

```python
primes=[True]*1000001
primes[0]=primes[1]=False
for i in range(2,1000001):
    if primes[i]:
        for j in range(i*i,1000001,i):
            primes[j] = False
l=[]
for i in range(2,1000001):
    if primes[i]:
        l.append(i)


n=int(input())
for i in range(n):
    k=int(input())
    left=0;right=len(l)-1
    while left<=right:
        mid=(left+right)//2
        if l[mid]<k//2:
            left=mid+1
        else:
            right=mid-1
    while primes[k-l[left]]==False :
        left-=1
    a=[l[left],k-l[left]]
    a.sort()
    print(*a)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M31296:“淹园”救援

http://cs101.openjudge.cn/practice/31296/

思路：



代码

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T31298:警察招募又来了

http://cs101.openjudge.cn/practice/31298/

思路：



代码

```python
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
            


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2026fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



