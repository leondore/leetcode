class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            shifted = nums.pop()
            nums.insert(0, shifted)
