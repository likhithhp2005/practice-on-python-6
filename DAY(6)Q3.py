# Iterative Divisor Check

n = 30
odd_sum = 0

for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 1:
        odd_sum += i

print(odd_sum)