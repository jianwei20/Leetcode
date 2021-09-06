class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last = '' if not strs else strs.pop()
        for i, c in enumerate(last):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return last[:i]
        return last