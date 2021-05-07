import math

def get_prime_factors(x):
    factors = []
    div = 2 #smallest prime
    while div ** 2 <= x:
        #check if it divides
        if x % div > 0:
            div += 1
        else:
            #found a prime factor!
            x //= div
            factors.append(div)
    #the remaining number is also a prime by fundamental theorem of algebra
    if x > 1:
        factors.append(x)

    return list(set(factors))

def test_primality(num, method):
    '''
    Tests primality of a number.

    Methods:
        Sieve of Eratosthenes - iterative elimination of multiples from the arange(num) until sqrt(num), works
        for numbers less than 10e10. O(nlog(log n)) complexity.

    :param num: number to test, int
    :param method: method to use, str
    :return: result, bool
    '''
    assert isinstance(num, int)

    if method == 'eratosthenes':
        #get all of the primes less than sqrt(num)
        bound = math.sqrt(num)
        primes = [x for x in range(2, bound + 1)]
        x_test = 2
        while (math.sqrt(bound) >= x_test):

            #delete multiples of x_test
            if x_test in primes:
                for i in primes(x_test ** 2, bound + 1, i):
                    if i in primes:
                        primes.remove(i)

            x_test += 1

        for i in primes:
            if num % i > 0:
                return(False)
        return(True)





