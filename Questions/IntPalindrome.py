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

        while tens >= 0:
            compare += (10**tens) * (temp % 10)
            tens -= 1
            temp /= 10

        return int(compare) == x

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        negative = 1
        if x < 0:
            negative = -1
        x = abs(x)
        compare = 0
        tens = math.floor(math.log10(x))

        while tens >= 0:
            compare += (10**tens) * (x % 10)
            tens -= 1
            x /= 10

        if compare >= 2**31:
            compare = 0

        return int(compare * negative)
        