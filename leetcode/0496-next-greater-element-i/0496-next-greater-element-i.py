class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic1 = {}
        for ind, val in enumerate(nums1):
            dic1[val] = ind
            
        
        ans = [-1] * len(nums1)
        for num in reversed(nums2):
            if num in dic1:
                while stack and stack[-1] <= num:
                    stack.pop()
                if stack and stack[-1] > num:
                    ans[dic1[num]] = stack[-1]
            
            stack.append(num)

        return ans
                
