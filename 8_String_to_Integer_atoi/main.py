class Solution:
    def myAtoi(self, s: str) -> int:
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        if(len(s) == 0):
            return 0
        ans = 0
        if s[0] == '-' :
            idx = 1
            while idx < len(s) and s[idx].isdigit():
                ans = ans * 10 + int(s[idx])
                idx += 1
                
            return -ans if ans <= 2 ** 31 else - 2 ** 31
        else:
            if s[0] == '+' :
                idx = 1
            else:
                idx = 0
            while idx < len(s) and s[idx].isdigit():
                ans = ans * 10 + int(s[idx])
                idx += 1
            return ans if ans < 2 ** 31 else 2 ** 31 - 1
