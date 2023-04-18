# Summation of primes

from math import sqrt

primes = [i for i in range(2, 2000000)]
print(primes)

for i in range(2, 2000000):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            primes.remove(i)
            break
                        
print(sum(primes))
