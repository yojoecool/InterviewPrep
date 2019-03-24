class QuickSort:
    def sort(self, array):
        if len(array) == 0 or len(array) == 1: return array

        firstGreater = -1
        pivot = array[0]

        for index in range(1, len(array)):
            if array[index] > pivot and firstGreater < 0:
                firstGreater = index
            elif array[index] < pivot and firstGreater > 0:
                temp = array[index]
                array[index] = array[firstGreater]
                array[firstGreater] = temp

                firstGreater += 1
        
        if firstGreater < 0:
            firstGreater = len(array)

        array[0] = array[firstGreater - 1]
        array[firstGreater - 1] = pivot

        firstHalf = self.sort(array[:firstGreater - 1])
        secondHalf = self.sort(array[firstGreater:])

        return firstHalf + [pivot] + secondHalf