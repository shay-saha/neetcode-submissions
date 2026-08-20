from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Counter = {}
        for c in nums:
            Counter[c] = Counter.setdefault(c,0)+1
            if Counter[c] > 1:
                return True
        return False
        
        
    
        