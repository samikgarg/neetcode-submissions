class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def add(currNum1, currNum2):
            num1Lst = list(currNum1)
            num2Lst = list(currNum2)
            carry = 0
            res = []
            while num1Lst or num2Lst or carry:
                digit1 = int(num1Lst[-1]) if num1Lst else 0
                digit2 = int(num2Lst[-1]) if num2Lst else 0
                currSum = digit1 + digit2 + carry
                res.append(str(currSum % 10))
                carry = currSum // 10
                if num1Lst:
                    num1Lst.pop()
                if num2Lst:
                    num2Lst.pop()
            return ''.join(res[::-1])
        
        res = ""
        place = 0
        for c1 in num1[::-1]:
            carry = 0
            currTerm = []
            for c2 in num2[::-1]:
                currProd = int(c1) * int(c2) + carry
                currTerm.append(currProd % 10)
                carry = currProd // 10
            if carry:
                currTerm.append(carry)
            currTerm.reverse()
            currTerm += [0] * place
            res = add(res, currTerm)
            place += 1
        return res

