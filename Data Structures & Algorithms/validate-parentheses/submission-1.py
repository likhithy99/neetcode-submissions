class Solution:
    def isValid(self, s: str) -> bool:
     stack = []
     matches = {')': '(', ']': '[', '}': '{'}
    
     for c in s:
        if c in matches:              
            if not stack or stack[-1] != matches[c]:
                return False
            stack.pop()
        else:                         
            stack.append(c)
    
     return len(stack) == 0
        