from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        counter_map = Counter(hand)
        hand.sort()

        heapq.heapify(hand)

        while hand:
            group_start = hand[0]
            for i in range(groupSize):
                elem = group_start + i
                # We don't have any consecutive card? Not a straight!
                if counter_map[elem] <= 0:
                    return False
                counter_map[elem] -= 1
            
            # Clean up the heap of used cards
            while hand and counter_map[hand[0]] == 0:
                heapq.heappop(hand)
        
        return True


