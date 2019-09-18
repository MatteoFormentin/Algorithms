

def binarySearch(array, to_find, start, end):
    if(end >= 1):

        mid = round(start + (end-1)/2)
        #print(array[start:end+1])

        if(to_find == array[mid]):
            return mid
        if(to_find < array[mid]):  # search left
            return binarySearch(array, to_find, start, mid-1)
        if(to_find > array[mid]):  # search right
            return binarySearch(array, to_find, mid+1, end)

    return -1


print(binarySearch([0, 4, 7, 9, 21, 45], 21, 0, 5))
