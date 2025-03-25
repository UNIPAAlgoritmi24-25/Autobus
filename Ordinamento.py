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

