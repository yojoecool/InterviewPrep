class HouseRobber:
  def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        prevHigh = nums[0]
        currHigh = max(nums[0], nums[1])
        index = 2

        while index < len(nums):
            temp = currHigh
            currHigh = max(prevHigh + nums[index], currHigh)
            prevHigh = temp
            index += 1

        return currHigh
