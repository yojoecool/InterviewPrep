class JumpGame:
    """
    Given that you need to get to the end of an array and each integer
    represents the max number of spaces you can jump, return a boolean
    for whether or not you can make it to the end of the array
    """
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
