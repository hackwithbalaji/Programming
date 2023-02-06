class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        substring = []
        for item in s:
            if item in substring:
                res = max(res, len(substring))
                substring = [] if substring.index(item) + 1 == len(substring) else substring[substring.index(item) + 1::]
            substring.append(item)
        res = max(res, len(substring))
        return res