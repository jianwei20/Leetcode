class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        s = 'A' + s + 'A'
        for i in range(1, len(s) - 1):
            if s[i] == 'I':
                if s[i + 1] != 'V' and s[i + 1] != 'X':
                    ans += 1
            
            elif s[i] == 'V':
                if s[i - 1] == 'I':
                    ans += 4
                else:
                    ans += 5

            elif s[i] == 'X':
                if s[i - 1] == 'I':
                    ans += 9
                elif s[i + 1] != 'L' and s[i + 1] != 'C':
                    ans += 10
                
            elif s[i] == 'L':
                if s[i - 1] == 'X':
                    ans += 40
                else:
                    ans += 50
                    
            elif s[i] == 'C':
                if s[i - 1] == 'X':
                    ans += 90
                elif s[i + 1] != 'D' and s[i + 1] != 'M':
                    ans += 100
                
            elif s[i] == 'D':
                if s[i - 1] == 'C':
                    ans += 400
                else:
                    ans += 500
                    
            else: # M
                if s[i - 1] == 'C':
                    ans += 900
                else:
                    ans += 1000
        return ans
