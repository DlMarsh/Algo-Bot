import time

def sort1 (arr: list) -> float:
    start = time.perf_counter()
    length = len(arr)
    for i in range(length):
        min_el = i
        for j in range(i, length):
            if arr[j] < arr[min_el]:
                min_el = j
        arr[i], arr[min_el] = arr[min_el], arr[i]
    finish = time.perf_counter()
    return((finish-start)*1000)

#------------------------------------------#

def heapify (l: int, n: int, arr: list) -> float:
    larq = l
    ld = 2*l + 1
    rd = 2*l + 2

    if ld < n and arr[l] < arr[ld]:
        larq = ld

    if rd < n and arr[larq] < arr[rd]:
        larq = rd

    if larq != l:
        arr[l], arr[larq] = arr[larq], arr[l]
        heapify(larq, n, arr)

def sort2 (arr:list):
    start = time.perf_counter()
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(i, n, arr)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i, arr)
    finish = time.perf_counter()
    return((finish-start)*1000)
