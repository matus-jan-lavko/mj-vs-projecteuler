#brute force method
def solve():
    fib = [1,2]
    while sum(fib) < 4e6:
        x_t = fib[-1] + fib[-2]
        fib.append(x_t)
    answer = sum(fib)
    print(str(answer))

if __name__ == '__main__':
    solve()