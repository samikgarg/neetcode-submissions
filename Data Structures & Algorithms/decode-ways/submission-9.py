class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s[0] == "0" else 1
        
        beforeLast = 0 if s[-1] == "0" else 1
        last = 0 if s[-2] == "0" else (beforeLast + (0 if int(s[len(s) - 2 : len(s)]) > 26 else 1))
        for i in range(len(s) - 3, -1, -1):
            if s[i] == "0":
                beforeLast, last = last, 0
                continue
            curr = last
            if int(s[i : i + 2]) <= 26:
                curr += beforeLast
            beforeLast, last = last, curr
        return last

        
        
