class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = [set(['()'])]
        for i in range(1, n):
            currSet = set()
            for s in parens[i - 1]:
                currSet.add('(' + s + ')')
            for j in range(i):
                for s1 in parens[j]:
                    for s2 in parens[i - j - 1]:
                        currSet.add(s1 + s2)
            parens.append(currSet)
        
        return list(parens[n - 1])