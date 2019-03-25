"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""
class Sums:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Explanation: The easiest way is the brute-force with a nested loop.
        To maintain an O(n) time complexity, you need to keep track of what value
        each element needs to reach the target and figure ou if that needed value
        exists in the rest of the array. To do this, I originally created an array of needed
        values for each index and also created a hashmap (dictionary) to keep the values
        that exist in the array as keys and the index as the value. So when trying to figure out if
        the value needed exists in the array, I can do so with O(1) lookup time complexity.
        """
        indicies = {}
        needed = []
        length = len(nums)

        for index in range(length):
            currVal = nums[index]
            neededVal = target - currVal

            # Added for 1 pass solution (same time complexity as 2 pass)
            if neededVal in indicies and index != indicies[neededVal]:
                return [index, indicies[neededVal]]
            
            needed.append(neededVal)
            indicies[currVal] = index

        # for index in range(length):
        #     neededVal = needed[index]
        #     if neededVal in indicies and index != indicies[neededVal]:
        #         return [index, indicies[neededVal]]

        return []
