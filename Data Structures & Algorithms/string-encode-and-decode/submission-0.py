class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs : 
            out += s
            out += "endofstring"
        return out

        
    def decode(self, s: str) -> List[str]:
        strs = s.split("endofstring")
        return strs[:-1]
