class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = [['()']]
        for i in range(n):
            parens.append([])
            
        
        
        
        
        
        if n == 1:
            return ['()']
        
        allParens = set()

        minusOne = self.generateParenthesis(n - 1)
        for item in minusOne:
            allParens.add('(' + item + ')')

        for i in range(1, n):
            setOne = self.generateParenthesis(i);
            setTwo = self.generateParenthesis(n - i);
            for item1 in setOne:
                for item2 in setTwo:
                    allParens.add(item1 + item2)
        
        return list(allParens)

            