class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        ch = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        ans = [ i for i in ch[int(digits[0])] ]
        
        if len(digits) == 1:
            return ans
        
        for i in range(1, len(digits)):
            ans = [ a1 + a2 for a1 in ans for a2 in ch[int(digits[i])] ]
            
        return ans
