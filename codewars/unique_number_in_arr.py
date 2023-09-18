def find_uniq(arr):
    arr_temp = list(set(arr))
    return arr_temp[0] if arr.count(arr_temp[0]) == 1 else arr_temp[1]


if __name__ == '__main__':
    print(find_uniq([1, 2, 1]))
    print(find_uniq([1, 1, 2]))
    print(find_uniq([2, 1, 1]))