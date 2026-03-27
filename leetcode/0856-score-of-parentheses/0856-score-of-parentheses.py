class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for b in s:
            if b == ")":
                if stack[-1] == 0:
                    val = stack.pop() + 1
                    stack[-1] += val
                else:
                    val = stack.pop() * 2
                    stack[-1] += val
            else:
                stack.append(0)

        return stack[-1]