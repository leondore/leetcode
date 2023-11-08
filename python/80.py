class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ptr = 0
        current = float("-inf")

        for idx, num in enumerate(nums):
            if idx < 2:
                ptr += 1
                current = num
                continue

            if num > current or num != nums[ptr - 2]:
                nums[ptr] = current = num
                ptr += 1

        return ptr
