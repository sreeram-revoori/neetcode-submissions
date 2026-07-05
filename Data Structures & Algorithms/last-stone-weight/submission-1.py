from bisect import insort
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones)>1:
             first = stones.pop()
             second = stones.pop()

             if first != second:
                insort(stones, first-second)

        return stones[0] if stones else 0