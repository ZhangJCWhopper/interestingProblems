import sys
import math
n = int(sys.stdin.readline().strip())
if n % 2 != 0:
    print(0)
    sys.exit(0)
down = 10
accum = 0
while True:
    crt = n // down
    if crt < 1:
        break
    accum += crt
    down *= 5
print(accum)
