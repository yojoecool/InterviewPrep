import sys
"""
Rotated Array Problems
"""
class RotatedArray:
    def minSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return sys.maxsize
        if length == 1:
            return nums[0]

        mid = length // 2

        leftMin = self.minSplit(nums[:mid])
        rightMin = self.minSplit(nums[mid:])

        if leftMin < rightMin:
            return leftMin
        return rightMin
    
    def minBSearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]

        mid = length // 2
        start = nums[0]
        end = nums[length - 1]

        if start < end:
            return start

        if nums[mid] > start and nums[mid] > end:
            return self.minBSearch(nums[mid + 1:])
        if nums[mid] < start and nums[mid] < end:
            return self.minBSearch(nums[:mid + 1])
        return self.minBSearch(nums[mid:])

    def binarySearch(self, nums, target, start = 0):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1

        mid = length // 2
        first = nums[0]
        last = nums[length - 1]

        if target == nums[mid]:
            return mid + start

        if first < last:
            if nums[mid] < target:
                return self.binarySearch(nums[mid + 1:], target, mid + start + 1)
            return self.binarySearch(nums[:mid], target, start)

        if first <= nums[mid]:
            if first <= target < nums[mid]:
                return self.binarySearch(nums[:mid], target, start)
            return self.binarySearch(nums[mid + 1:], target, start + mid + 1)

        if nums[mid] < target <= last:
            return self.binarySearch(nums[mid + 1:], target, start + mid + 1)
        return self.binarySearch(nums[:mid], target, start)

