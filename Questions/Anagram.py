class Anagram:
    def isAnagram(self, s1, s2):
        allChars = {}
        for c in s1:
            if c in allChars:
                allChars[c] += 1
            else:
                allChars[c] = 1

        for c in s2:
            if c in allChars:
                if allChars[c] == 0:
                    return False
                allChars[c] -= 1
            else:
                return False

        return True