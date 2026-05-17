class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False

        for s_i, t_i in zip(s, t):
            s_dict[s_i] = s_dict.get(s_i, 0) + 1
            t_dict[t_i] = t_dict.get(t_i, 0) + 1
        return s_dict == t_dict
        