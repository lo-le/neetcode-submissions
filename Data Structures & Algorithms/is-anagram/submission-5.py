class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramletters = []
        if len(s.strip()) != len(t.strip()) : return False
        if set(s) != set(t) : return False

        for c in s : 
            if c in t : 
                placement = t.find(c)
                t = t[:placement] + t[placement+1:]
            else : 
                return False
        
        return True
            