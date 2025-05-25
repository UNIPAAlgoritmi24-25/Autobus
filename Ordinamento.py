import random

def dataset(taglie=None, negativi=True):
    n_max = +1500
    n_min = -1500
    if not negativi:
        n_min = 0

    output = []
    if not taglie:
        taglie = [10, 100, 1000, 5000, 10000]
    for taglia in taglie:
        temp = []
        for _ in range(taglia):
            temp.append(random.randint(n_min, n_max))
        output.append(temp)
    return output

def counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(0, len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    n = len(arr)        
    for i in range(1, n):      
        key = arr[i]        
        j = i-1
        while j >= 0 and key < arr[j]:      
            arr[j+1] = arr[j]       
            j -= 1
        arr[j+1] = key     
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  
        sinistra = [x for x in arr if x < pivot]
        centro = [x for x in arr if x == pivot]
        destra = [x for x in arr if x > pivot]
        return quicksort(sinistra) + centro + quicksort(destra)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def get_alg():
    return [
        {"N": "bubble_sort", "F": bubble_sort},
        {"N": "insertion_sort", "F": insertion_sort},
        {"N": "quicksort", "F": quicksort},
        {"N": "merge_sort", "F": merge_sort},
        {"N": "counting_sort", "F": counting_sort},
    ]
