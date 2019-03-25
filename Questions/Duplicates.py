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
        dupSet = set()

        for num in nums:
            if num in dupSet:
                return True
            dupSet.add(num)

        return False
