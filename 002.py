#brute force method
def solve():
    fib = [1,2]
    while fib[-1] < 4e6:
        x_t = fib[-1] + fib[-2]
        fib.append(x_t)

    even = [x for x in fib if x % 2 == 0]
    answer = sum(even)
    print(str(answer))

if __name__ == '__main__':
    solve()