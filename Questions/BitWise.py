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
    
    """
    Given a positive integer N, find and return the longest distance between two consecutive 1's
    in the binary representation of N.

    If there aren't two consecutive 1's, return 0.
    
    example 1:
        Input: 22
        Output: 2
        Explanation: 
        22 in binary is 0b10110.
        In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
        The first consecutive pair of 1's have distance 2.
        The second consecutive pair of 1's have distance 1.
        The answer is the largest of these two distances, which is 2.
    example 2:
        Input: 8
        Output: 0
        Explanation: 
        8 in binary is 0b1000.
        There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
    """
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxLength = 0
        start = -1
        index = 0
        
        while N != 0:
            if N % 2:
                if start >= 0 and index - start > maxLength:
                    maxLength = index - start
                start = index
            N //= 2
            index += 1
            
        return maxLength
