class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict: dict[int, int] = {}

        for idx in range(0, len(nums)):
            partner = target - nums[idx]

            if partner in nums_dict:
                return [idx, nums_dict[partner]]

            nums_dict[nums[idx]] = idx

        return []
