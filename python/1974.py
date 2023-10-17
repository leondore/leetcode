class Solution:
    def __init__(self):
        self.first = ord("a")
        self.last = ord("z")

    def calcClockwise(self, current: int, target: int) -> int:
        if target > current:
            return target - current
        else:
            return (self.last - current) + (target - self.first) + 1

    def calcCounterClockwise(self, current: int, target: int) -> int:
        if target < current:
            return current - target
        else:
            return (self.last - target) + (current - self.first) + 1

    def minTimeToType(self, word: str) -> int:
        current_char = "a"
        seconds = 0

        for char in word:
            if char == current_char:
                seconds += 1
            else:
                clockwise_time = self.calcClockwise(ord(current_char), ord(char))
                counter_clockwise_time = self.calcCounterClockwise(
                    ord(current_char), ord(char)
                )
                seconds += (
                    clockwise_time
                    if clockwise_time <= counter_clockwise_time
                    else counter_clockwise_time
                )
                seconds += 1

                current_char = char

        return seconds
