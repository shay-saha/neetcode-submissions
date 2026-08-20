class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = list(s)
        lis = list()
        for c in sl:
            if c.isalnum():
                lis.append(c.lower())    
        if lis[::-1] == lis:
            return True

        return False
