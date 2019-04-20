"""
Given an array of integers,
find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Examples:
Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Duplicates:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Explanation: Using a set, we can see what values already exist in
        the array as we iterate through wih O(1) retrieval. If the set already contains
        the value we're at, we return True to denote that a duplicate is found. Otherwise,
        we return False at the end after we've made it through the entire list without
        finding a duplicate.
        """

        """
        Alt Solution:
        dupSet = set(nums)
        return len(dupSet) != len(nums)

        Smaller code, but time complexity should be the same O(n) as solution below
        """

        dupSet = set()

        for num in nums:
            if num in dupSet:
                return True
            dupSet.add(num)

        return False

    """
    Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

    Find all the elements that appear twice in this array.

    Could you do it without extra space and in O(n) runtime?

    Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]
    """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[index] = abs(nums[index]) * -1

        return ans
        
    """
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

    Find all the elements of [1, n] inclusive that do not appear in this array.

    Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

    Example:

    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]
    """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
