class BinarySearch:
    def search(self, array, target, start = 0):
        if len(array) == 0: return -1

        mid = len(array) // 2

        if array[mid] == target: return start + mid
        if array[mid] < target: return self.search(array[mid + 1:], target, start + mid + 1)
        return self.search(array[:mid], target, start)