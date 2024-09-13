"""
This .py file performs merge sort of 20 random numbers
"""
import rand


def merge_sort(arr1):
    """
    Merge sort.

    Args:
        arr (array): array of numbers.
        

    Returns:
        array: sorted array.
    """
    if len(arr1)==0:
        return arr1
    if len(arr1) == 1:
        return arr1
    half = len(arr1) // 2
    return recombine(merge_sort(arr1[:half]), merge_sort(arr1[half:]))


def recombine(left_arr, right_arr):
    """
    Merging left half and right half
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    return merge_arr


arr = rand.random_array([None] * 20)
print(arr)
arr_out = merge_sort(arr)
print(arr_out)
