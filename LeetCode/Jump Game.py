class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i = i+1
                continue
            
            j = i-1
            helper = False
            while j >= 0:
                if nums[j] + j > i or nums[j] + j == len(nums) - 1:
                    helper = True
                    break
                j -= 1
            
            if not helper:
                return False
            i += 1

        return True