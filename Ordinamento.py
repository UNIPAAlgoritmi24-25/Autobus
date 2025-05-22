
import random


def dataset(taglie=None, negativi = True):
    n_max = +1500
    n_min = -1500
    if not negativi:
        n_min = 0


    output = []
    if not taglie:
        taglie = [10,100,1000, 5000]
    for taglia in taglie:
        temp = []
        for _ in range(taglia):
            temp.append(random.randint(n_min, n_max))
        output.append(temp)
    return output

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
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
     
    if n <= 1:
        return      

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
        return quicksort(sinistra) + centro+ quicksort(destra)
