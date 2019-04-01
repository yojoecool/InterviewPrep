def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        jewels = set(J)

        for stone in S:
            if stone in jewels:
                count += 1

        return count
