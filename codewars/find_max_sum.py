def find_max_sum(n):
    res = 0
    for a1 in range(n, 0, -1):
        for a2 in range(n, 0, -1):
            for a3 in range(n, 0, -1):
                if (a1 + a2) % 2 == 0 and (a2 + a3) % 3 == 0 and (a1 + a2 + a3) % 5 == 0:
                    a = a1 + a2 + a3
                    if a > res:
                        res = a
    print(res)


print(find_max_sum(0))
print(find_max_sum(3))
print(find_max_sum(10000))


# test_cases = [
#     (0, 0),
#     (3, 5),
#     (4, 10),
#     (5, 10),
#     (6, 15),
#     (7, 15),
#     (8, 20),
#     (9, 25),
#     (30, 90),
#     (29, 85),
#     (28, 80),
#     (10000, 29995),
# ]
