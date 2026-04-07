class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        
        r = n - 1
        while r >= 0:
            while stack and temperatures[stack[-1]] <= temperatures[r]:
                stack.pop()

            if stack and temperatures[stack[-1]] > temperatures[r]:
                ans[r] = stack[-1] - r

            stack.append(r)
            r -= 1
            
        return ans