class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counta = {}
        countb = {}
        for a in range(len(s)):
            counta[s[a]] = counta.get(s[a],0)+1
            countb[t[a]] = countb.get(t[a],0)+1
        return counta == countb
        #accessing elements of the string using their index instead of directly
