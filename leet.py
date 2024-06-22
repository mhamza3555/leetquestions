class Solution:
    def lengthOfLongestSubstring(self, s):
        unique_chars = set(s)
        return len(unique_chars)

sol = Solution()
string = "pwwkew"
print(sol.lengthOfLongestSubstring(string))
