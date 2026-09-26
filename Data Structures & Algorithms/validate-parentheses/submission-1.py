class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in closing:
                if len(stack) == 0 or stack.pop() != closing[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0