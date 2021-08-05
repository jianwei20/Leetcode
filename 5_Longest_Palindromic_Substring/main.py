class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)
        ans_left = 0
        ans_right = len(s)
        max_length = 0
        #odd
        for i in range(s_length):
            tmp = 1
            tmp_left = i
            tmp_right = i
            while tmp_left - 1 >= 0 and tmp_right + 1 < s_length and s[tmp_left - 1] == s[tmp_right + 1]:
                tmp_left -= 1
                tmp_right += 1
                tmp += 2
            if tmp >= max_length:
                max_length = tmp
                ans_left = tmp_left
                ans_right = tmp_right
            
        #even
        for i in range(s_length - 1):
            if s[i] == s[i + 1]:
                tmp = 2
                tmp_left = i
                tmp_right = i + 1
                while tmp_left - 1 >= 0 and tmp_right + 1 < s_length and s[tmp_left - 1] == s[tmp_right + 1]:
                    tmp_left -= 1
                    tmp_right += 1
                    tmp += 2
                if tmp >= max_length:
                    max_length = tmp
                    ans_left = tmp_left
                    ans_right = tmp_right
        return s[ans_left:ans_right + 1]
