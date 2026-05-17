class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')','[':']', '{':'}'}
        reversed_brackets = {v:k for k,v in brackets.items()}
        if len(s) == 1:
            return False

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            
            elif len(stack) != 0 and  reversed_brackets[char] == stack.pop():
                pass
            else:
                return False
            
        return len(stack) == 0