def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    # if n == 1 or n == 0:
    #     return 1
    # temp = 1
    # for num in range(1, n + 1):
    #     temp *= num
    # return temp
    return 1 if n <= 1 else n * factorial(n - 1)
if __name__ == '__main__':
    print(factorial(5))
    print(factorial(1))
    print(factorial(-25))