# QUICKSORT
# How it Works: First, calculate the middle of array. then put on left all element minor than array[middle], on right the major.
# Then recursively apply it to the left and right arrays. If array size is one, it is ordinated.


def quickSort(array):
    if len(array) == 1:
        return array

    m = int(len(array) / 2-1)
    #Actually inefficient by a memory point of view: it would be best to work irectly on the array itself
    l = []
    r = []
    for i in array:
        if i < array[m]:
            l.append(i)

        if i > array[m]:
            r.append(i)

    l.append(array[m])
    return quickSort(l) + quickSort(r)
