
def get_mean(arr,x,y):
    if x == 1 or y == 1 or x > len(arr) or y > len(arr):
        return -1
    a = (sum(arr[:x ]) / len(arr[:x]) + sum(arr[-y:]) / len(arr[-y:])) / 2
    print(arr[:x])
    return a

print(get_mean([1,-1,2,-1],2,3))

    

