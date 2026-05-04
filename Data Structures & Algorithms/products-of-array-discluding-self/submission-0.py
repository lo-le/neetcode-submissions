class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countzeroes = nums.count(0)
        if countzeroes >= 2 : #2+ zeroes always full 0s product
            return [0] * len(nums)

        for num in nums : 
            if num != 0: 
                product *= num
        print(product)

        res = []
        for i in range(len(nums)) : 
            if nums[i] != 0: 
                if countzeroes >= 1 : 
                    res.append(0)
                else :
                    res.append(product // nums[i])
            else : 
                res.append(product)

        return res