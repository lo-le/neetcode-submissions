class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []
        for s in strs :
            count = [0] * 26
            for c in s : 
                count[ord(c) - ord("a")] += 1
            print(count)
            groups[tuple(count)].append(s)
            
        print(groups)
        for i in groups.values() : 
            res.append(i)
        return res