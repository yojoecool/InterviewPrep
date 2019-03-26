"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of
nums except nums[i].

Note: Please solve it without division and in O(n).

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Input: [1,2,3,4,0]
Output: [0,0,0,0,24]

Input: [0,1,2,3,4,0]
Output: [0,0,0,0,0,0]
"""
class ProductExceptSelf:
    def __init__(self, nums):
        self.nums = nums

    def withDiv(self):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        answer = []
        zeroCount = 0

        for num in self.nums:
            if num != 0:
                total *= num
            else:
                zeroCount += 1

        for num in self.nums:
            if zeroCount > 1:
                answer.append(0)
            elif zeroCount > 0 and num != 0:
                answer.append(0)
            elif zeroCount > 0 and num == 0:
                answer.append(total)
            else:
                answer.append(total / num)

        return answer
    
    def withoutDiv(self):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(self.nums)
        right = [1] * len(self.nums)
        
        left.append(1)
        
        index = 1
        while index < len(self.nums):
            left[index] = left[index - 1] * self.nums[index - 1]
            index += 1
        
        index = len(self.nums) - 2
        while index >= 0:
            right[index] = right[index + 1] * self.nums[index + 1]
            index -= 1
            
        index = 0
        answer = []
        while index < len(self.nums):
            answer.append(left[index] * right[index])
            index += 1

        return answer
