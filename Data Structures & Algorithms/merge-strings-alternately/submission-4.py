class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        
        for i in zip(word1, word2):
            result.append(i[0])
            result.append(i[1])
        
        if len(word1) > len(word2):
            for i in word1[len(word2):]:
                result.append(i)
        elif len(word1) < len(word2):
            for i in word2[len(word1):]:
                result.append(i)


        return ''.join(result)
