class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        currSol = []
        def backtrack(index):
            if index == len(s):
                res.append(currSol[:])
            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    currSol.append(s[index : i + 1])
                    backtrack(i + 1)
                    currSol.pop()
        
        backtrack(0)
        return res


        
        