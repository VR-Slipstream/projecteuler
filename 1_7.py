# Multiples of 3 or 5

def total(x):
    total = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(total(1))


# Even Fibonacci numbers

sum = 0
def even_fib(m, n):
    global sum
    term = m + n
    print(term)
    m = n
    n = term
    
    if m % 2 == 0:
        sum += m
    
    if term < 4000000:
        even_fib(m, n)
    return "SUM = " + str(sum)
    
print(even_fib(1, 2))


# Largest prime factor

from math import sqrt

x = 600851475143

factors = []

for i in range(1, x//2 + 1):
    if x % i == 0:
        print("Status_factors, ", i)
        factors.append(i)

primefactors = factors[::-1]
        
for i in factors:
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            print("Status, ", i)
            primefactors.remove(i)
            break

print(f"Largest Prime factor = {primefactors.pop(0)}")        


# Largest palindrome product

pals = []
def large_pal():
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if str(i*j) == str(i*j)[::-1]:
                pals.append(i*j)
    return max(pals)
        
print(large_pal())


# Smallest multiple

ran = []
def small_num(x):
    num = 1
    while len(ran) != x:
        for i in range(1, x + 1):
            if num % i != 0:
                ran.clear()
                num += 1
                break
            else:
                ran.append(i)
    return num
        
print(small_num(20))


# Sum square difference

def diff(x):
    return sum_sq(x) ** 2 - sq_sum(x)

def sq_sum(x):
    if x == 1:
        return 1
    else:
        return x ** 2 + sq_sum(x-1)
    
def sum_sq(x):
    if x == 1:
        return 1
    else:
        return x + sum_sq(x-1)

print(diff(100))


# 10001st prime

primes = []
num = 2
def prime_pos(x):
    global num
    while len(primes) < x:
        primes.append(num)
        for i in range(2, x//2):
            if num % i == 0 and num != i:
                primes.remove(num)
                break
        
        num += 1
    return primes[-1]

print(prime_pos(10001))
