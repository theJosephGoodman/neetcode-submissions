class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_refined =''.join(ch.lower() for ch in s if ch.isalnum())

        for i in range(len(s_refined)//2):
            if s_refined[i] == s_refined[-1-i]:
                pass
            else:
                return False
        return True