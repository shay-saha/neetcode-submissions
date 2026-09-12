class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack1 = []
        if len(s)%2 != 0:
            return False
        for p in s:
            if p in pairs.values():
                stack1.append(p)
            if p in pairs:
                if len(stack1) == 0:
                    return False
                if stack1.pop() != pairs[p]:
                    return False
        return len(stack1) == 0
                
