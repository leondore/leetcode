class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            nums1.clear()
            nums1.extend(nums2)
            return

        del nums1[m:]

        i = j = 0
        while j < n:
            while i < len(nums1):
                if nums2[j] < nums1[i]:
                    nums1.insert(i, nums2[j])
                    break
                i += 1
            if i == len(nums1):
                nums1.insert(i, nums2[j])
            j += 1
