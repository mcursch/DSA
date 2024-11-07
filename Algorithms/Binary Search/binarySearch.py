def binarySearch(arr, target):
    left, right = 0, len(arr) -1
    #do less than or equal because if you have an array of length 1, l == r
    while left <= right:
        #get middle of current left and right indices, i.e. if l = 50, r = 100, gives you 75
        mid = (left + right) //2

        if arr[mid] == target:
            return mid
        #if arr[mid] < target i.e. comparing 5 to 9, 9 is bigger, so it must be on the right side of mid,
        # so adjust left
        if arr[mid] < target:
            left = mid+1
        # if arr[mid] < target i.e. comparing 12 to 9, 9 is smaller, so it must be on the left side of mid,
        # so adjust right
        if arr[mid] > target:
            right = mid - 1

    return -1


digits = list(range(1,101))
value = 9

print(binarySearch(digits, value))
