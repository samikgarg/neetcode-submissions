class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = []
            for i in range(26):
                counts.append(0)
            for c in word:
                counts[ord(c) - ord('a')] += 1
            
            if str(counts) in groups:
                groups[str(counts)].append(word)
            else:
                groups[str(counts)] = [word]
        
        results = []
        for group in groups.values():
            results.append(group)
        
        return results