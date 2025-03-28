
import random


def dataset(taglie=None):
    output = []
    if not taglie:
        taglie = [10,100,1000, 5000]
    for taglia in taglie:
        temp = []
        for _ in range(taglia):
            temp.append(random.randint(-1500, +1500))
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