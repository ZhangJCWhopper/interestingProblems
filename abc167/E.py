import sys
l = sys.stdin.readline().strip()
N, M, K = map(int, l.split())
comb_quick = {}
mod = 998244353
C = [1]
# python pow is much faster, and pow(x, y, [z]) supports x ** y mod z
"""
To make the (Combination of x from N-1) faster, using the Fermat's little theorem
if p is a prime number, and gcd(a, p) = 1 then a ^ (p-1) = 1 mod p
so x / y mod p => x * 1/y mod p 
1/y mod p can be y ** (p-2) mod p
"""
for i in range(1, (N-1) // 2 + 2):
    # iteratively compute N-1 C x using N-1 C x-1
    next = C[-1] * (N-i) * pow(i, mod-2, mod)
    C.append(next % mod)

res = 0

for x in range(K+1):
    # if there is x pairs of adjecent blocks of the same color
    # then the blocks be assigned to N-x groups
    crt =  (pow(M-1, N-x-1, mod) * M) % mod 
    crt %= mod
    #print("start")
    idx = min(x, N-1-x)
    # how many possible ways to assign the pairs
    crt *= C[idx]
    #print("end")
    crt %= mod
    res += crt
    res %= mod

print(res)