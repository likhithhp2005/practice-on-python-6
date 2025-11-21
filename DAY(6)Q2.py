# Optimized Divisor Pairing

import math
n = 30
odd_sum = 0

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if i % 2 == 1:
            odd_sum += i
        if (n // i) % 2 == 1 and n // i != i:
            odd_sum += n // i

print(odd_sum)