import heapq, itertools
from collections import deque
G = {'S':['A','B'],'A':['C','D'],'B':['D','E'],'C':['G'],'D':['G'],'E':['G'],'G':[]}
W = {('S','A'):2,('S','B'):3,('A','C'):4,('A','D'):3,('B','D'):2,('B','E'):6,('C','G'):3,('D','G'):5,('E','G'):1}
H = {'S':7,'A':5,'B':4,'C':2,'D':4,'E':1,'G':0}
def bfs(s,g):
    q=deque([[s]]);seen={s};order=[]
    while q:
        p=q.popleft();n=p[-1];order.append(n)
        if n==g:return order,p
        for m in G[n]:
            if m not in seen:seen.add(m);q.append(p+[m])
def dfs(s,g):
    st=[[s]];seen=set();order=[]
    while st:
        p=st.pop();n=p[-1]
        if n in seen:continue
        seen.add(n);order.append(n)
        if n==g:return order,p
        for m in reversed(G[n]):
            if m not in seen:st.append(p+[m])
def dls(n,g,l,order,path):
    order.append(n)
    if n==g:return path+[n]
    if l==0:return None
    for m in G[n]:
        r=dls(m,g,l-1,order,path+[n])
        if r:return r
def ids(s,g):
    tot=[]
    for l in range(10):
        o=[];r=dls(s,g,l,o,[]);tot.append((l,o))
        if r:return tot,r
def best(s,g,astar):
    c=itertools.count();pq=[(H[s],next(c),0,[s])];closed=set();order=[]
    while pq:
        f,_,gc,p=heapq.heappop(pq);n=p[-1]
        if n in closed:continue
        closed.add(n);order.append(n)
        if n==g:return order,p,gc
        for m in G[n]:
            g2=gc+W[(n,m)]
            heapq.heappush(pq,((g2 if astar else 0)+H[m],next(c),g2,p+[m]))
print('BFS',bfs('S','G'))
print('DFS',dfs('S','G'))
print('IDS',ids('S','G'))
print('Greedy',best('S','G',False))
print('A*',best('S','G',True))
# all path costs
def paths(n,p,c):
    if n=='G':print(p,c);return
    for m in G[n]:paths(m,p+[m],c+W[(n,m)])
paths('S',['S'],0)
# admissibility check: true cost to G
import functools
@functools.lru_cache(None)
def hstar(n):
    return 0 if n=='G' else min(W[(n,m)]+hstar(m) for m in G[n])
print({n:(H[n],hstar(n)) for n in G})
# 8-puzzle heuristics
start=[[2,8,3],[1,6,4],[7,0,5]];goal=[[1,2,3],[8,0,4],[7,6,5]]
pos={goal[i][j]:(i,j) for i in range(3) for j in range(3)}
h1=sum(1 for i in range(3) for j in range(3) if start[i][j] and start[i][j]!=goal[i][j])
h2=sum(abs(i-pos[start[i][j]][0])+abs(j-pos[start[i][j]][1]) for i in range(3) for j in range(3) if start[i][j])
print('h1',h1,'h2',h2)
# water jug 4,3 -> 2 in 4-jug
def jug():
    s=(0,0);q=deque([(s,[s])]);seen={s}
    while q:
        (a,b),p=q.popleft()
        if a==2:return p
        nxt=[(4,b),(a,3),(0,b),(a,0),(a-min(a,3-b),b+min(a,3-b)),(a+min(b,4-a),b-min(b,4-a))]
        for x in nxt:
            if x not in seen:seen.add(x);q.append((x,p+[x]))
p=jug();print('jug',len(p)-1,p)
# hill climbing 1D landscape
L=[3,5,8,6,4,7,9,12,10,2]
def hc(i):
    path=[i]
    while True:
        nb=[j for j in (i-1,i+1) if 0<=j<len(L)]
        b=max(nb,key=lambda j:L[j])
        if L[b]<=L[i]:return path,L[i]
        i=b;path.append(i)
for s in (0,4,6):print('hc',s,hc(s))
# 8-puzzle optimal moves BFS
def solve(st):
    t=lambda b:tuple(x for r in b for x in r)
    s=t(start);g=t(goal);q=deque([(s,0)]);seen={s}
    while q:
        b,d=q.popleft()
        if b==g:return d
        z=b.index(0);r,c=divmod(z,3)
        for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<3 and 0<=nc<3:
                l=list(b);k=nr*3+nc;l[z],l[k]=l[k],l[z];nb=tuple(l)
                if nb not in seen:seen.add(nb);q.append((nb,d+1))
print('8puzzle optimal',solve(start))
