class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []
        ignores = 0
        for i, c in enumerate(s):
            if c == '(':
                openStack.append(i)
            if c == '*':
                starStack.append(i)
            if c == ')':
                if openStack:
                    openStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        for i in range(len(openStack) - 1, -1, -1):
            if starStack and starStack[-1] > openStack[i]:
                starStack.pop()
            else:
                return False
        return True
        
            