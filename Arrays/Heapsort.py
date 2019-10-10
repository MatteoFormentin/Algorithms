# HEAPSORT
# How it Works: it build the Max Heap and then expoloit that ordinated data structure.
#
# HEAP: A binary tree where root is bigger than all child of all sublevel. Can be rappresented by an array were root is in first cell, then first level children, then second...
# The foundamental property is that if i is the subtree root, left element is at 2*i+1 index and right at 2*i+2
#        10(0)
#       /  \
#     5(1)  3(2)     =>  [10 5 3 4 1]
#     /   \
# 4(3)    1(4)
#
# To make a heap from an array starting from the level before leafs ones current root should be compared with the leaf and swapped if minor than one
# than the modified subtree should be heapified again with recursion, that will put the old root down to its place. The last level checked is the first
# root node, so the build start from last array element to the first.
# Note that the heapify algorithm required the two subtree to be heaps since it only checked the modified subtree and not the others,
# so it's necessary to first heapify the lowest levels then go to the highest
#
# Once build the heap, the heap sort algorithm simply take the first element of the array (the max of array) and  put it to the end, than it rebuild the max heap
# Reducing the array of one element (the last wich is ordered)


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find the largest of child and put as root of subtree.
    # Note that the tree is not binary search so left or right value makes no difference, they must only be minor than the root
    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        # Swap with last element
        temp = array[largest]
        array[largest] = array[i]
        array[i] = temp

        # Heapify the modified subtree
        heapify(array, n, largest)


def heapSort(array):
    # Actually we start from the half of the array since leaf would be on the right half (2 * len/2 +1) and should be ignored
    for i in range(int(len(array)/2 - 1), -1, -1):
        heapify(array, len(array), i)

    for i in range(int(len(array)) - 1, - 1, -1):
        # On 0 there is the max, oni is the last element of subarray
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        heapify(array, i, 0)

    return array