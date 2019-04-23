class AllModes:
    """
    Return list of modes in array
    """
    def returnAll(self, arr):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return arr[0]
        
        maxCount = 0
        allNums = {}
        answer = []

        for num in arr:
            if num in allNums:
                allNums[num] = allNums[num] + 1
            else:
                allNums[num] = 1

            if allNums[num] == maxCount:
                answer.append(num)
            elif allNums[num] > maxCount:
                answer = [num]
                maxCount = allNums[num]

        return answer

    """
    Return singular mode when gauranteed to 
    """
    def oneMode(self, arr):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return arr[0]

        allNums = {}

        for num in arr:
            if num in allNums:
                allNums[num] = allNums[num] + 1
            else:
                allNums[num] = 1

            if allNums[num] == len(arr) // 2:
                return num

        return None
