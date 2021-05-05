#brute force method
def solve():
    mults = [x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)]
    answer = sum(mults)

    print(str(answer))

if __name__ == '__main__':
    solve()


