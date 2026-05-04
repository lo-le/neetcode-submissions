class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #val : i

        for i, n in enumerate(nums) : 
                remainder = target - nums[i]
                if remainder in map :
                    r1 = map[remainder]
                    r2 = i
                    if r1 != r2 :
                        return [r1, r2]
                map[n] = i