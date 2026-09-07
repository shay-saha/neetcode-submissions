from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicta = Counter(s)
        dictb = Counter(t)
        if dicta == dictb:
            return True
        return False
        