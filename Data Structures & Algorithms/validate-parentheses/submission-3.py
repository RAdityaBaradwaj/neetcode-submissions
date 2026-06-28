class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corr = {"{":"}","[":"]","(":")"}
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            else:
                if stack and c == corr[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True