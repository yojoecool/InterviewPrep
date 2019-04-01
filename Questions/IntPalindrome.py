import math

class IntPalindrome:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False

        compare = 0
        temp = x
        tens = math.floor(math.log10(x))
        count = 0

        while count <= tens:
            compare += (10**tens) * (temp % 10)
            tens -= 1
            temp /= 10

        return int(compare) == x
