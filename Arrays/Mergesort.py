#   MERGESORT
#   How it Works: it split the array into half recursively and than ordinate chunks
#   merging them with min check from smaller lenght to higher


def mergeSort(array):
    if len(array) == 0 or len(array) == 1:
        return array

    mid = round(len(array) / 2)

    # Recursion: first left branch, than right one
    left = mergeSort(array[0:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)  # Merge the result and go up


def merge(left, right):
    #print("to merge"+str(left) + "   " + str(right))
    merged = []
    j = 0
    i = 0
    while i + j < len(left) + len(right):
        # One array as been completly checked -> other remaining are for sure bigger (since are ordinated) -> fill merged without checking
        if i == len(left):
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged

        # Same but for other array case
        if j == len(right):
            while i < len(left):
                merged.append(left[i])
                i += 1
            return merged

        # Standard case search in pairs the minimum -> fill with them -> move only min array by one -> repeat
        if(left[i] <= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    return merged
