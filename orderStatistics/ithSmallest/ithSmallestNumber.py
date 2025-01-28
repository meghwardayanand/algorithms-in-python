import random


class IthSmallestNumber:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def findIthNumber(self, i):
        if i > self.length or i < 1:
            raise IndexError

        return self.random_select(0, self.length - 1, i)

    def random_partition(self, p, q):
        index = random.randint(p, q)
        self.arr[p], self.arr[index] = self.arr[index], self.arr[p]

        x = self.arr[p]
        i = p

        for j in range(p + 1, q + 1):
            if self.arr[j] <= x:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[p], self.arr[i] = self.arr[i], self.arr[p]

        return i

    def random_select(self, p, q, i):
        if p == q:
            return self.arr[p]

        r = self.random_partition(p, q)
        k = r - p + 1
        if i == k:
            return self.arr[r]

        if i < k:
            return self.random_select(p, r - 1, i)

        return self.random_select(r + 1, q, i - k)
