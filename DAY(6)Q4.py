# Using List Comprehension
n = 30
odd_sum = sum([i for i in range(1, n + 1) if n % i == 0 and i % 2 == 1])
print(odd_sum)