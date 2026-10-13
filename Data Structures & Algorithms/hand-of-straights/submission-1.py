class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True
        
        hand.sort()

        groups = {}
        for card in hand:
            if card not in groups:
                groups[card] = []
            if card - 1 in groups and groups[card - 1]:
                currGroupSize = groups[card - 1].pop()
                if currGroupSize + 1 < groupSize:
                    groups[card].append(currGroupSize + 1)
            else:
                groups[card].append(1)
        
        return not any(groups.values())

        # groups = {3 : [3, 2]}

