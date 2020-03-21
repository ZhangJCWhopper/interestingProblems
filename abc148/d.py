import sys

n = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().split())
nums = list(nums)
if 1 not in nums:
    print(-1)
    sys.exit(0)
crt = 1

for i in range(n):
    if nums[i] == crt:
        crt += 1
    
print(n - crt + 1)
