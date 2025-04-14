import math

x = int(input())
count = 0

for a in range(1, int(math.isqrt(x)) + 1):
    b_squared = x - a*a
    b = int(math.isqrt(b_squared))
    if b >= a and b*b == b_squared:
        count += 1

print(count)
