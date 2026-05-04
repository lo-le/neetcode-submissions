class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramletters = []
        if len(s.strip()) != len(t.strip()) : return False
        if set(s) != set(t) : return False

        for i in range(len(s)) : 
            if s[i] in t : 
                placement = t.find(s[i])
                t = t[:placement] + t[placement+1:]
            else : 
                return False
        
        return True
            