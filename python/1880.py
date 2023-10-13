class Solution:
    def getNumericValue(self, word: str) -> int:
        num = 0
        power = len(word) - 1
        for char in word:
            num += (ord(char) - 97) * 10**power
            power -= 1
        return num

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.getNumericValue(firstWord) + self.getNumericValue(
            secondWord
        ) == self.getNumericValue(targetWord)
