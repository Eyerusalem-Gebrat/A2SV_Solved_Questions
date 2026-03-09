class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(" : ")", "{" : "}", "[" : "]"}
        for bracket in s:
            if bracket in dic:
                stack.append(bracket)
            else:
                if not stack: return False
                else:
                    if bracket == dic[stack[-1]]:
                        stack.pop()
                    else:
                        return False

        return not stack
