from sorting.sort import Sort


class MergeSort(Sort):

    def sort(self):
        self.arr = self.mergeSort(self.arr)
        return self.arr

    def merge(self, left_arr, right_arr):
        result = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] < right_arr[right_idx]:
                result.append(left_arr[left_idx])
                left_idx += 1
            else:
                result.append(right_arr[right_idx])
                right_idx += 1

        result.extend(left_arr[left_idx:])
        result.extend(right_arr[right_idx:])

        return result

    def mergeSort(self, arr):
        arr_length = len(arr)
        if arr_length <= 1:
            return arr

        mid_index = arr_length // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]

        left_arr = self.mergeSort(left_arr)
        right_arr = self.mergeSort(right_arr)

        arr = self.merge(left_arr, right_arr)

        return arr
