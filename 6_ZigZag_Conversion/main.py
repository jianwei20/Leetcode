class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        s_length = len(s)
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[0::2] + s[1::2]
        elif numRows >= s_length:
            return s
        else:
            step = (numRows - 1) * 2
            for i in range(numRows):
                idx = i
                ans += s[idx]
                if idx == 0 or idx == numRows - 1:
                    while idx + step < s_length:
                        idx += step
                        ans += s[idx]
                else:
                    while idx + step < s_length:
                        idx += step
                        ans += s[idx - 2 * i]
                        ans += s[idx]
                    if idx + step - 2 * i < s_length:
                        ans += s[idx + step - 2 * i]
        return ans
