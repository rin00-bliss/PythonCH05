def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5) +1):
        if n % 1 == 0:
            return False 
    return True
def print_primes(n):
    for i in range(2,n):
        if is_prime(i):
            print(i, end=" ")
    print()
def get_primes(n):
    primes = []
    for i in range (2, n):
        if is_prime(i):
            primes.append(i)
    return primes