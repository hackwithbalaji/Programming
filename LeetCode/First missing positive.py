class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        helper = dict.fromkeys(range(1, len(nums) + 1), True)
        m = 1

        while i < len(nums):
            if nums[i] > 0:
                if nums[i] in helper:
                    del helper[nums[i]]
                    m = max(m, nums[i])
            i += 1
        
        if len(helper) > 0:
            return min(helper.keys())
        return m+1