
import math

from sorting.sort import Sort


class HeapSortDescending(Sort):

    def sort(self):
        self.heapSort()
        return self.arr

    def minHeapify(self, i):
        l = 2*i
        r = 2*i + 1
        smallest = None

        if l < self.length and self.arr[l] < self.arr[i]:
            smallest = l
        else:
            smallest = i

        if r < self.length and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.minHeapify(smallest)

    def buildMinHeap(self):
        i = math.floor(self.length/2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def heapSort(self):
        self.buildMinHeap()
        i = self.length - 1
        while i >= 1:
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.length -= 1
            i -= 1
            self.minHeapify(0)
