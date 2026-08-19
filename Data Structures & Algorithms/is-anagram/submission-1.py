class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        for c in s:
            counts[c] = counts.setdefault(c,0)+1
        for a in t:
            countt[a] = countt.setdefault(a,0)+1
        if counts == countt:
            return True
        else:
            return False
        

