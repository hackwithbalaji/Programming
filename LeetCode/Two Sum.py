class Solution:
    # def find_pair(self, nums, num1, num2):
    #     i = 0
    #     res = []
    #     while i < len(nums) and len(res) !=2:
    #         if nums[i] == num1:
    #             res.append(i)
    #             i = i+1
    #             continue
    #         elif nums[i] == num2:
    #             res.append(i)
    #             i = i+1
    #             continue
    #         else:
    #             i = i+1
    #     return res

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # while i< len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         j = j+1
        #     i = i + 1
        # iteration = int(target/2)
        # start = 0
        # end = target - 1
        # for i in range(0,iteration):
        #     res = Solution().find_pair(nums, start, end)
        #     if(len(res) == 2):
        #         return res
        #     start = start + 1
        #     end = end - 1
        helper = {}
        for i in range(0, len(nums)):
            helper[nums[i]] = i
        for i in range(0, len(nums)):
            if target - nums[i]  in helper and i != helper[target - nums[i]]:
                return [i, helper[target - nums[i]]]

    
            

    