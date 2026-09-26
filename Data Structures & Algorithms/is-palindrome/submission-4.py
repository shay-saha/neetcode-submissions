class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = list()
        for c in s:
            if c.isalnum():
                lis.append(c.lower()) 
        m = list(lis)  
        lis.reverse()
        if m == lis:
            return True

        return False

        #brute force solution but takes too much space from preprocessing string, removing unalphanum, converting to lowercase etc
