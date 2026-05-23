class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif (c == ')' and stack[len(stack)-1] == '(') or (c == ']' and stack[len(stack)-1] == '[') or (c == '}' and stack[len(stack)-1] == '{'):
                stack.pop()
            else:
                stack.append(c)
            
        if len(stack) == 0:
            return True
        else:
            return False