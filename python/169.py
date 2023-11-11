class Solution:
    def majorityElement(self, nums):
        numsCounts = {}
        largest = None

        for num in nums:
            numsCounts[num] = numsCounts[num] + 1 if num in numsCounts else 1
            if not largest or numsCounts[num] > numsCounts[largest]:
                largest = num

        return largest
