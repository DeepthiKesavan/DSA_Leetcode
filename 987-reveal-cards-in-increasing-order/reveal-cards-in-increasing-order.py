from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        q = deque(range(len(deck)))
        result = [0] * len(deck)
        for card in deck:
            index = q.popleft()
            result[index] = card
            if q:
                q.append(q.popleft())
        return result
