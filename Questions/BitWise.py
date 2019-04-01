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

    def reverseBits(self, n):
        answer = 0
        bitCount = 0
        while bitCount < 32:
            leftOver = n % 2
            n >>= 1
            answer <<= 1
            answer += leftOver
            bitCount += 1

        return answer

    def decToBin(self, n):
        if n == 0:
            return "0"

        answer = ""
        while n != 0:
            nextBit = n % 2
            answer = str(nextBit) + answer
            n //= 2

        return answer
