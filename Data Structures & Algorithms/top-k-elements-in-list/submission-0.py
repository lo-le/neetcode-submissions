class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        res = []
        for n in nums : 
            if n in map : 
                map[n] += 1
            else : 
                map[n] = 1
        i = k 
        while i > 0 : 
            maxkey = max(map, key=map.get) 
            res.append(maxkey)
            del(map[maxkey])
            i -= 1
        return res