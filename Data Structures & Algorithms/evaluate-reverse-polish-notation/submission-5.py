class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                l1 = int(stack.pop())
                l2 = int(stack.pop())
                if token == '+':
                    stack.append(l2+l1)
                elif token == '-':
                    stack.append(l2-l1)
                elif token == '*':
                    stack.append(l2*l1)
                elif token == '/':
                    if l2/l1 < 0:
                        stack.append(math.ceil(l2/l1))
                    else:
                        stack.append(math.floor(l2/l1))
            
        return stack[0]