import numpy as np

def solve():
    sum_of_squares = np.sum(np.power(np.arange(101),2))
    square_of_sum = np.power(np.sum(np.arange(101)),2)
    print(sum_of_squares - square_of_sum)


if __name__ == '__main__':
    solve()