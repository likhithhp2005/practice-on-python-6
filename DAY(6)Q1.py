# Python Program for Find Sum of Odd Factors of a Number
# Formula-based Approach
import math
n = 30
res = 1

while n % 2 == 0:
    n //= 2

for i in range(3, int(math.sqrt(n)) + 1):
    curr_sum = 1
    curr_term = 1
    while n % i == 0:
        n //= i
        curr_term *= i
        curr_sum += curr_term
    res *= curr_sum

if n >= 2:
    res *= (1 + n)

print(res)