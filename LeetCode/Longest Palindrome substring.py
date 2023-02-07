class Solution:
    def palindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)
        count = 0
        start = 0
        end = 0
        while(i < len(s)):
            if s[i] == s[j-1]:
                if self.palindrome(s[i:j]):
                    if count < len(s[i:j]):
                        count = len(s[i:j])
                        start = i
                        end = j
            if i == j:
                i = i+1
                j = len(s)
                continue
            elif i>j:
                break
            j = j - 1
        return s[start:end]