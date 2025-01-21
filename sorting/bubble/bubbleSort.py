from sorting.sort import Sort


class BubbleSort(Sort):
    def sort(self):
        for i in range(self.length):
            is_swapped = False
            for j in range(0, self.length - i - 1):
                if self.arr[j] > self.arr[j+1]:   # if found larger item before smaller one
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]   # then swap them
                    is_swapped = True

            if not is_swapped:   # if rest of the items are sorted.
                break

        return self.arr
