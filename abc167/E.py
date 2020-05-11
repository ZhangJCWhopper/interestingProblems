import sys
l = sys.stdin.readline().strip()
N, M, K = map(int, l.split())
comb_quick = {}
mod = 998244353
C = [1]
for i in range(1, (N-1) // 2 + 2):
    next = C[-1] * (N-i) * pow(i, mod-2, mod)
    C.append(next % mod)

res = 0

for x in range(K+1):
    crt =  (pow(M-1, N-x-1, mod) * M) % mod 
    crt %= mod
    #print("start")
    idx = min(x, N-1-x)
    crt *= C[idx]
    #print("end")
    crt %= mod
    res += crt
    res %= mod

print(res)