class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxTriplet = [0, 0, 0]

        for triplet in triplets:
            canUse = True
            for i in range(3):
                if triplet[i] > target[i]:
                    canUse = False
                    break
            if not canUse:
                continue
            for i in range(3):
                maxTriplet[i] = max(maxTriplet[i], triplet[i])
        
        return target == maxTriplet