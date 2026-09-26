class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: (abs(x)//x) * (abs(y)//y) * (abs(x) // abs(y)) if x != 0 else 0
        }

        for item in tokens:
            if item in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operations[item](num2, num1))
            else:
                stack.append(int(item))
        
        return stack.pop()
