class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _nums2 = set(nums2)
        ans = []
        for num in set(nums1):
            if num in _nums2:
                ans.append(num)

        return ans