def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    mtr = ''
    for i in range(n // 2 + 1):
        mtr += ' ' * (n//2 - i)+ '*' * (i * 2 + 1) + '\n'
    for i in range(n // 2 - 1, -1, -1):
        mtr += ' ' * (n//2 - i) + '*' * (i * 2 + 1) + '\n'
    return mtr

if __name__ == "__main__":
    print(diamond(3))
    print(diamond(5))
    print(diamond(2))
    print(diamond(-3))
    print(diamond(11))
    print(diamond(7))