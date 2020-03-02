import sys

"""
Friends network, a typical problem of "Disjoint-set / Union-find"
I usedf graph and DFS, but for large dataset it is slow
"""

line = sys.stdin.readline().strip()
n,m,k = map(int, line.split())
roots = [-1]*n
linked = [0]*n
def find_root(x):
    if roots[x] < 0:
        return x
    else:
        roots[x] = find_root(roots[x])
        return roots[x]
def unite(x, y):
    x = find_root(x)
    y = find_root(y)
    if (x==y):
        return
    if roots[x] > roots[y]:
        c, d = y,x
        x,y = c,d
    roots[x] += roots[y]
    roots[y] = x

for i in range(m):
    line = sys.stdin.readline().strip()
    a,b = map(int, line.split())
    c, d = a-1,b-1
    linked[c] += 1 
    linked[d] += 1
    unite(c,d)
#print(roots)
blacks = [[]for i in range(n)]
for i in range(k):
    line = sys.stdin.readline().strip()
    a,b = map(int, line.split())
    c,d = a-1, b-1
    blacks[c].append(d)
    blacks[d].append(c)
res = []
for i in range(n):
    r = -roots[find_root(i)] - 1 - linked[i]
    for one in blacks[i]:
        if find_root(one) == find_root(i):
            r -= 1
    res.append(r)
    
print (" ".join(map(str, res)))
