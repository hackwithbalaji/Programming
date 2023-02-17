from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        # Method1 using Counter
        m = 0
        v = 0
        nums = Counter(nums)
        for item in nums:
            if nums[item] > m:
                m = nums[item]
                v = item
        
        return v

        #Method2 without Counter
        # helper = {}
        # m = 0
        # value = nums[0]
        # for i in nums:
        #     if i in helper:
        #         helper[i] = helper[i] + 1
        #         if helper[i] > m:
        #             m = helper[i]
        #             value = i
        #     else:
        #         helper[i] = 1
        
        # return value
