def sort(arr: list) -> list:
    n = len(arr)
    maxi = max([len(str(i)) for i in arr])

    for i in range(maxi):
        buf = [[] for _ in range(10)]
        for num in arr:
            buf[(num//(10**i)) % 10].append(num)
        arr = [x for queue in buf for x in queue] #Не пустные элементы
    return arr
