class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        seq = sorted(set(nums))
        res = []
        highest = 0
        for n in seq : 
            if len(res) == 0 or n == res[-1] + 1 : 
                res.append(n)
            else : 
                highest = max(highest, len(res))
                res = [n]

        return max(highest, len(res))