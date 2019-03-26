class MaxSubArray:
    def __init__(self, nums):
        self.nums = nums

    def sum(self):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(self.nums) == 0:
            return 0
        if len(self.nums) == 1:
            return self.nums[0]

        prevHigh = self.nums[0]
        high = self.nums[0]

        for index in range(1, len(self.nums)):
            prevHigh = max(self.nums[index], prevHigh + self.nums[index])
            high = max(high, prevHigh)

        return high

    def product(self):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(self.nums) == 0:
            return 0
        if len(self.nums) == 1:
            return self.nums[0]


        prevHigh = self.nums[0]
        prevMin = self.nums[0]
        high = self.nums[0]

        for index in range(1, len(self.nums)):
            tempHigh = max(
                [self.nums[index], prevHigh * self.nums[index], prevMin * self.nums[index]]
            )
            tempMin = min(
                [self.nums[index], prevMin * self.nums[index], prevHigh * self.nums[index]]
            )

            prevHigh = tempHigh
            prevMin = tempMin
            high = max(high, prevHigh)

        return high
