class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
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
            currString = ""
            for i in range(index, len(s)):
                currString += s[i]
                if isPalindrome(currString):
                    currSol.append(currString)
                    backtrack(i + 1)
                    currSol.pop()
        
        backtrack(0)
        return res


        
        