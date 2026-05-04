class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r : 
            while self.alphaNum(s[l]) == False and l < r : 
                l += 1
            while self.alphaNum(s[r]) == False and r > l : 
                r -= 1
            if s[l].lower() != s[r].lower() : 
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c) : 
        return(
            ord("A") <= ord(str(c)) <= ord("Z") or 
            ord("a") <= ord(str(c)) <= ord("z") or 
            ord("0") <= ord(str(c)) <= ord("9")
        )
