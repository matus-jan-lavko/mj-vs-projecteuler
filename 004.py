from itertools import permutations

def solve():
    n1 = 100
    n2 = 100
    candidate = n1 * n2
    for i in range(899):
        n2 = 100
        for j in range(899):
            ans = n1 * n2

            if str(ans) == str(ans)[::-1] and ans > candidate:
                candidate = ans

            n2 += 1
        n1 += 1
        print(candidate)

if __name__ == '__main__':
    solve()