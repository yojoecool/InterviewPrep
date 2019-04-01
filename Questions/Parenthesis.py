class Parenthesis:
  def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openPar = { '(', '{', '[' }
        closedPar = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        charList = []

        while len(s) > 0:
            curr = s[0]
            if curr in openPar:
                charList.append(curr)
            else:
                if len(charList) == 0 or closedPar[curr] != charList.pop():
                    return False
            s = s[1:]

        if len(charList) > 0:
            return False

        return True
