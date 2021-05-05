from utils import get_prime_factors

#brute force method
def solve():
    number = 600851475143
    primes = get_prime_factors(number)
    answer = max(primes)
    print(answer)

if __name__ == '__main__':
    solve()