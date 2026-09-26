class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            currDigit = digits[i] + carry
            res.append(currDigit % 10)
            carry = currDigit // 10
        while carry:
            res.append(carry % 10)
            carry //= 10
        res.reverse()
        return res
        