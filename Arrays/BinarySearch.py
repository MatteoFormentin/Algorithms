# BINARY SEARCH ALGORITHM
# Recursive search on a sorted array. Simple principle: on an ordered array, if the to be find element is greater 
# than the middle one it would be for sure on the right partition, else on the left one. 
# Note: End is len(array)-1


def binarySearch(array, to_find, start, end):
    if(end >= 1):
        mid = round(start + (end-1)/2)
        if(to_find == array[mid]): #Recursion until the array is so small that the middle is the value to find
            return mid
        if(to_find < array[mid]):  # search left
            return binarySearch(array, to_find, start, mid-1)
        if(to_find > array[mid]):  # search right
            return binarySearch(array, to_find, mid+1, end)
    return -1
