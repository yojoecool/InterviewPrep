"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"abcabcbb"      3
"bbbbb"         1
"pwwkew"        3
"cdd"           2
"abba"          2
"tmmzuxt"       5
"bbtablud"      6
"""

class LongestSubstring:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        length = 0
        maxLength = 0

        for index in range(len(s)):
            currLetter = s[index]
            if currLetter not in letters or letters[currLetter] < index - length:
                letters[currLetter] = index
                length += 1
            else:
                maxLength = max(length, maxLength)
                length = index - letters[currLetter]
                letters[currLetter] = index

        maxLength = max(length, maxLength)

        return maxLength
