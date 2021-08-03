class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0
        ans = 0
        start_index = 0
        d = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                if start_index <= d[s[i]]:
                    start_index = d[s[i]] + 1
                d[s[i]] = i
            if (i - start_index + 1) > ans:
                ans = (i - start_index + 1)
        return ans
