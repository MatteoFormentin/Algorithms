# BINARY SEARCH ALGORITHM
# Recursive search on a sorted array
# Note: End is len(array)-1


def binarySearch(array, to_find, start, end):
    if(end >= 1):
        mid = round(start + (end-1)/2)
        if(to_find == array[mid]):
            return mid
        if(to_find < array[mid]):  # search left
            return binarySearch(array, to_find, start, mid-1)
        if(to_find > array[mid]):  # search right
            return binarySearch(array, to_find, mid+1, end)
    return -1
