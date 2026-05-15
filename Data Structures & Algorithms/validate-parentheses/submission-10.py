class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        reversed_brackets =  {')':'(', '}':'{', ']':'['}
        if len(s) == 1:
            return False
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                # если стек пуст
                if not stack:
                    return False
                top = stack.pop()

                # проверяем соответствие
                if top != reversed_brackets[char]:
                    return False
        return len(stack) == 0