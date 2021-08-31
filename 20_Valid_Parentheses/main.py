class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        else:
            idx = -1
            stack = ['' for i in range(len(s))]
            for i in range(len(s)):
                if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    idx += 1
                    stack[idx] = s[i]
                else:
                    if (s[i] == ')' and stack[idx] == '(') or (s[i] == '}' and stack[idx] == '{') or (s[i] == ']' and stack[idx] == '['):
                        idx -= 1
                    else:
                        return False
            if idx == -1:
                return True
            else:
                return False
