from searching.search import Search


class SequentialSearch(Search):

    def search(self, x):
        is_found = False
        i = 0
        while i < self.length:
            if self.arr[i] == x:
                is_found = True
                break
            i += 1

        return self.arr[i] if is_found else None
