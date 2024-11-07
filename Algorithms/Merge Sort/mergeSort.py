def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    l_recurs = merge_sort(left)
    r_recurs = merge_sort(right)

    return merge(l_recurs, r_recurs)

def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)