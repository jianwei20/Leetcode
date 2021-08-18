class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def fcn(s, left, right, string):
            if left > 0:
                fcn(s + 1, left - 1, right, string + '(')
            
            if right > 0 and s > 0:
                fcn(s - 1, left, right - 1, string + ')')
                
            if s == 0 and left == 0 and right == 0:
                ans.append(string)
        
        fcn(0, n, n, '')
                
        return ans
