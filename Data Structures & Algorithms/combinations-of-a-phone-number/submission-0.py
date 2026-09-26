class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digitMap = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
            }
        
        rest = self.letterCombinations(digits[1:])
        if not rest:
            rest = [""]
        res = []
        for combo in rest:
            for alph in digitMap[digits[0]]:
                res.append(alph + combo)
        return res