from sorting.sort import Sort


class QuickSort(Sort):

    def sort(self):
        self.quickSort(0, self.length)
        return self.arr

    def partition(self, p, q):
        x = self.arr[p]      # pivot element as first element of the arr
        i = p

        for j in range(p + 1, q):
            if self.arr[j] <= x:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
    
        return i

    def quickSort(self, p, q):
        if p < q:
            r = self.partition(p, q)
            self.quickSort(p, r)
            self.quickSort(r + 1, q)
