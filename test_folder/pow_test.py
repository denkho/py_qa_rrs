def my_pow(number, expon):
    res = 1
    for i in range(expon):
        res *= number
    return res


print(my_pow(2, 2))
print(my_pow(2, 8))