PARENS = {"(": ")", "{": "}", "[": "]"}


class Solution:
    def __init__(self):
        self.parens = []

    def isValid(self, s: str) -> bool:
        for char in s:
            if char in PARENS.keys():
                self.parens.append(char)
            else:
                if len(self.parens) == 0:
                    return False

                if PARENS[self.parens[-1]] == char:
                    self.parens.pop()
                else:
                    return False

        if len(self.parens) == 0:
            return True
        return False
