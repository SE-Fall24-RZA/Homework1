import rand


def merge_sort(arr):
    if len(arr)==0:
        return arr
    if len(arr) == 1:
        return arr
    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1
    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + i] = rightArr[i]

    for i in range(leftIndex, len(leftArr)):
        mergeArr[i + rightIndex] = leftArr[i]

    return mergeArr


arr = rand.random_array([None] * 20)
print(arr)
arr_out = merge_sort(arr)
print(arr_out)
