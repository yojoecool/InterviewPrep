class MergeSort:
    def merge(self, a, b):
        sorted = []

        while len(a) > 0 and len(b) > 0:
            if a[0] < b[0]: sorted.append(a.pop(0))
            else: sorted.append(b.pop(0))
        
        return sorted + a + b

    def sort(self, array):
        if len(array) == 0 or len(array) == 1: return array

        mid = len(array) // 2

        firstHalf = self.sort(array[:mid])
        secondHalf = self.sort(array[mid:])
 
        return self.merge(firstHalf, secondHalf)

    def sort_three_way(self, array):
        if len(array) <= 1: return array

        third = len(array) // 3
        second_third = (len(array) * 2) // 3

        firstThird = self.sort_three_way(array[:third])
        secondThird = self.sort_three_way(array[third:second_third])
        lastThird = self.sort_three_way(array[second_third:])

        firstMerged = self.merge(firstThird, secondThird)

        return self.merge(firstMerged, lastThird)