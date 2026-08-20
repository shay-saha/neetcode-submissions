class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = list(s)
        lis = list()
        for c in sl:
            if c.isalnum():
                lis.append(c.lower()) 
        m = list(lis)  
        lis.reverse()
        if m == lis:
            return True

        return False
