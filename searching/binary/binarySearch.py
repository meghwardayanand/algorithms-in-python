from searching.search import Search


class BinarySearch(Search):

    def search(self, x):
        isFound = False
        left = 0
        right = self.length - 1
        mid = (right - left) // 2

        while (not isFound) and (left <= right):
            mid = left + (right - left) // 2

            if self.arr[mid] == x:
                isFound = True
                break
            elif self.arr[mid] > x:
                right = mid - 1
            elif self.arr[mid] < x:
                left = mid + 1

        return self.arr[mid] if isFound else None
