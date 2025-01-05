from searching.search import Search


class SequentialSearch(Search):

    def search(self, x):
        isFound = False
        i = 0
        while i < self.length:
            if self.arr[i] == x:
                isFound = True
                break
            i += 1

        return self.arr[i] if isFound else None
