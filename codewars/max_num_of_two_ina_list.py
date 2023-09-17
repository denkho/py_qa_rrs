def adjacent_element_product(array):
    """Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

    Args:
        array (list): Array/list size is at least 2.
    """
    mul_max = array[0] * array[1]
    for i in range(1, len(array) - 1):
        temp = array[i] * array[i + 1]
        if temp > mul_max:
            mul_max = temp
    return mul_max

if __name__ == '__main__':
    print(adjacent_element_product([1, 2, 3]))
    