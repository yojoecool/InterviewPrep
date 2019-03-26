import sys

class FindMinArray:
    def rotated(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -sys.maxsize - 1
        if length == 1:
            return nums[0]

        mid = length // 2

        leftMin = self.rotated(nums[:mid])
        rightMin = self.rotated(nums[mid:])

        if leftMin < rightMin:
            return leftMin
        return rightMin
