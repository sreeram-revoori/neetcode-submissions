class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for idx,val in enumerate(nums):
            compliment =  target - val
            if compliment in seen:
                return [seen[compliment],idx]
            seen[val] = idx
        return []
