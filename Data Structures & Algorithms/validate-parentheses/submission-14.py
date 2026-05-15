class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'[':']', '{':'}', '(':')'}
        reversed_brackets = {v:k for k,v in brackets.items()}
        stack = []
        for i in range(len(s)):
            if len(s)==1:
                return False
            
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if len(stack) == 0 : return False

                last_element = stack.pop()

                if last_element == reversed_brackets[s[i]]:
                    pass
                else:
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False