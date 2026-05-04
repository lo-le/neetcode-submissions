class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)) :
            val = nums[i] 
            map[val] = i
        print(map)

        for i in range(len(nums)) : 
                remainder = target - nums[i]
                if remainder in map :
                    r1 = i
                    r2 = map[remainder]
                    if r1 != r2 :
                        return [r1, r2]