class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return self.val_pal(s, l+1, r) or self.val_pal(s, l, r-1)
            l= l + 1 
            r = r - 1
        return True
        
        


    def val_pal(self, s, l , r):
        l_in = l
        r_in = r


        while l_in < r_in:
            if s[l_in] != s[r_in]:
                return False
            l_in = l_in + 1
            r_in = r_in - 1

        return True