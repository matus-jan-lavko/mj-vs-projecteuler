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
