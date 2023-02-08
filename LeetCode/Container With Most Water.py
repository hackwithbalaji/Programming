class Solution:
    def maxArea(self, height: List[int]) -> int:

        m = 0
        i = 0
        j = len(height) - 1
        while i < j:
            m = max(m, min(height[i], height[j]) *(j-i))
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return m
    
        #Other solutions
    
        # count = 0
        # i = 0
        # while i < len(height):
        #     j = i + 1
        #     while j < len(height):
        #         if height[j] <= height[i]:
        #             count = max(count, height[j] * (j-i))
        #         else:
        #             count = max(count, height[i] * (j-i))
        #         j = j + 1
        #     i = i+1
        
        # return count

        # m = 0
        # i = 0
        # length = len(height)
        # while i < length:
        #     j = length-1
        #     while j > i:
        #         prev = (j + 1)
        #         if prev > (length - 1):
        #             prev = length - 1
                
        #         # if height[prev] > height[j]:
        #         #     break
        #         # else:
        #         temp = min(height[i], height[j])
        #         m = max(m, temp *(j-i))
        #         j = j-1
        #     i = i + 1
        # return m

        # m = 0
        # i = 1
        # first_low = { "value":  height[0], "index": 0}
        # second_low = { "value":  height[0], "index": 0}
        # length = len(height)
        # while i < length:
        #     m = max(max( (i - first_low["index"]) * min(first_low["value"],height[i]),  m) , (i - second_low["index"]) * min(second_low["value"],height[i]) )
        #     if first_low["value"] < height[i] and second_low["value"] < height[i]:
        #         first_low["value"] = second_low["value"]
        #         first_low["index"] = second_low["index"]
        #         second_low["value"] = height[i]
        #         second_low["index"] = i
        #     elif first_low["value"] < height[i]:
        #         first_low["value"] = height[i]
        #         first_low["index"] = i
        #     i = i + 1
        # return m
