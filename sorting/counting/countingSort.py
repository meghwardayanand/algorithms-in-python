from sorting.sort import Sort


class CountingSort(Sort):
    def sort(self):
        if self.length <= 1:
            return self.arr

        k = max(self.arr) + 1
        c = [0] * k
        b = [None] * self.length

        for i in self.arr:
            c[i] += 1

        for j in range(1, k):
            c[j] = c[j] + c[j-1]

        j = self.length - 1
        while j >= 0:
            b[c[self.arr[j]] - 1] = self.arr[j]
            c[self.arr[j]] -= 1
            j -= 1

        return b
