import math

from sorting.sort import Sort


class HeapSortAscending(Sort):

    def sort(self):
        self.heapSort()
        return self.arr

    def maxHeapify(self, i):
        l = 2*i
        r = 2*i + 1
        largest = None

        if l < self.length and self.arr[l] > self.arr[i]:
            largest = l
        else:
            largest = i

        if r < self.length and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        i = math.floor(self.length/2)
        while i >= 0:
            self.maxHeapify(i)
            i -= 1

    def heapSort(self):
        self.buildMaxHeap()
        i = self.length - 1
        while i >= 1:
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.length -= 1
            i -= 1
            self.maxHeapify(0)
