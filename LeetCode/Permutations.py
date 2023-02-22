import math
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [nums,[nums[1], nums[0]]]

        i = 0 
        res = []
        while i < len(nums):
            temp = self.permute(nums[0:i] + nums[i+1:len(nums)])
            for item in temp:
                item.append(nums[i])
            res.extend(temp)
            i += 1
        
        return res