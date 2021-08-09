class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31 - 1  else 0
        else:
            return -int(str(x)[1:][::-1]) if -int(str(x)[1:][::-1]) >= -2**31 else 0

