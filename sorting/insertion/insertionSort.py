from sorting.sort import Sort


class InsertionSort(Sort):
    def sort(self):
        for i in range(1, self.length):
            current_element = self.arr[i]
            j = i - 1

            while j >= 0 and self.arr[j] > current_element:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = current_element

        return self.arr
