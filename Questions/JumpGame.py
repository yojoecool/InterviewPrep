class JumpGame:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = len(nums) - 1
        lastIndex = index

        while index >= 0:
            if lastIndex - index <= nums[index]:
                lastIndex = index
            index -= 1

        return lastIndex == 0
