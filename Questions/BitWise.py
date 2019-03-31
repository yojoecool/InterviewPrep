class BitWise:
    """
    Find number of '1' bits in integer
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n != 0:
            count += n % 2
            n /= 2

        return count
