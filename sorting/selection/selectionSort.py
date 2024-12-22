from sorting.sort import Sort


class SelectionSort(Sort):
    def sort(self):
        for i in range(self.length - 1):
            min_at_index = i
            for j in range(i + 1, self.length):
                if self.arr[j] < self.arr[min_at_index]:
                    min_at_index = j
        
            self.arr[i], self.arr[min_at_index] = self.arr[min_at_index], self.arr[i]

        return self.arr
