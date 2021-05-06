# We can use the fact that a least common divisor of two rational numbers is defined as
# LCM(x,y) = x * y / GCD(x, y) and that it can be nested (it is commutative and associative).

import math

def solve():
    num = 1
    for i in range(1,21):
        num = num * i // math.gcd(i,num)
    print(num)


if __name__ == '__main__':
    solve()