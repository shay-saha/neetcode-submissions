class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftpointer = 0
        rightpointer = len(s) -1 
        while leftpointer< rightpointer:
            while leftpointer< rightpointer and not s[leftpointer].isalnum():
                leftpointer+=1
            while leftpointer< rightpointer and not s[rightpointer].isalnum():
                rightpointer-=1
            if s[leftpointer].lower() == s[rightpointer].lower():
                leftpointer+=1
                rightpointer-=1
            else:
                return False
        return True
        #acvoids extra space, single pass using two pointers

        