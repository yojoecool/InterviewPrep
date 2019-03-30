class PyramidArray:
    def minValue(self, arr):
        first = arr[0]
        last = arr[len(arr) - 1]

        if first > last: return last
        return first

    def maxIndex(self, arr, start = 0):
        if len(arr) == 1:
            return start

        mid = len(arr) // 2

        if mid == len(arr) - 1:
            if arr[mid] > arr[mid - 1]:
                return start + mid
            return self.maxIndex(arr[:mid], start)

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return start + mid

        if arr[mid] > arr[mid - 1]:
            return self.maxIndex(arr[mid + 1:], start + mid + 1)

        return self.maxIndex(arr[:mid], start)

    def sorted(self, arr):
        if len(arr) <= 1:
            return arr
        
        split = self.maxIndex(arr)

        firstHalf = 0
        secondHalf = len(arr) - 1
        answer = []

        while firstHalf < split and secondHalf >= split:
            if arr[firstHalf] < arr[secondHalf]:
                answer.append(arr[firstHalf])
                firstHalf += 1
            else:
                answer.append(arr[secondHalf])
                secondHalf -= 1

        return answer + arr[firstHalf:split] + arr[split:secondHalf][::-1]
