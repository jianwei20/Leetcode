class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        flag = True
        minLen = 500
        for i in range(len(strs)):
            if minLen > len(strs[i]):
                minLen = len(strs[i])
            if minLen == 0:
                return ""

        for k in range(minLen):
            for i in range(len(strs)-1):
                if strs[i][k] != strs[i+1][k]:
                    flag = False
                    break
            if flag:
                ans += strs[0][k]
            else:
                break
            
        return ans
