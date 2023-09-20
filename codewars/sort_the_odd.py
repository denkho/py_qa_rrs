def sort_array(source_array: list) -> list:
    indexes, odds = [], []
    for i, v in enumerate(source_array):
        if v % 2 != 0:
            indexes.append(i)
            odds.append(v)
    odds.sort()
    print(odds, indexes)
    for i, v in enumerate(indexes):
        source_array[v] = odds[i]
        
    return source_array


if __name__ == "__main__":
    print(sort_array([7, 1]))
    print(sort_array([5, 8, 6, 3, 4]))
