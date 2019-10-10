# PRIORITY QUEUE
# Implemention of a priority queue using heap. pop()valways return the gratest of the queue element. For sake of semplicity
# it is implemented for number but can easily extended to any kind of object by adding a java style comparator


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, el):
        self.heap.append(el)
        #Swap el with its father until its new father is greater
        while self.heap[(el.getIndex() -2)/2] < el:
            pass

    def pop(self):
        # Swap first(max) with last element
        temp = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)]
        self.heap[len(self.heap)] = temp
        # Pop last element and remove it (get the max)
        el = self.pop()

        # Heapify the tree. Note that all of subtree are heap apart of the root, so calling heapify on the root will put
        # it on the right place
        self.heapify(0)
        return el

    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Find the largest of child and put as root of subtree.
        # Note that the tree is not binary search so left or right value makes no difference, they must only be minor than the root
        if left < len(self.heap) and heap[left] > heap[largest]:
            largest = left

        if right < len(self.heap) and heap[right] > heap[largest]:
            largest = right

        if largest != i:
            # Swap
            temp = heap[largest]
            heap[largest] = heap[i]
            heap[i] = temp

            # Heapify the modified subtree
            heapify(self, largest)
