class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = nums[len(nums) - 1]
        idx = 0
        current = float("-inf")

        for num in nums:
            if current == last:
                break

            if num > current:
                nums[idx] = current = num
                idx += 1

        return idx
