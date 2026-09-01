from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = Counter(nums)
        return any(c>1 for c in result.values())
        