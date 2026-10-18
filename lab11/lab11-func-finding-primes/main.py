'''
lab11-func-finding-primes
'''
# YOUR CODE HERE

primes = [2]


def is_prime(num):
    global primes

    for prime in primes:
        if num % prime == 0:
            return False

    return True


n = int(input())

for i in range(3, n + 1):
    if is_prime(i):
        primes.append(i)

print(primes)
