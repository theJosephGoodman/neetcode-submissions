class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}

        for s_char, t_char in zip(s,t):
            if s_char in s_freq:
                s_freq[s_char]+=1
            else:
                s_freq[s_char]=1

            if t_char in t_freq:
                t_freq[t_char]+=1
            else:
                t_freq[t_char]=1
        
        if s_freq==t_freq:
            return True
        else:
            return False