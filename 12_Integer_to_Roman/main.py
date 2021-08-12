class Solution:
    def intToRoman(self, num: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        while num > 0 :
            if num >= 1000: # M
                ans += 'M' * (num // 1000)
                num = num % 1000
            elif num >= 900: # CM
                ans += 'CM' * (num // 900)
                num = num % 900
            elif num >= 500: # D
                ans += 'D' * (num // 500)
                num = num % 500
            elif num >= 400: # CD
                ans += 'CD' * (num // 400)
                num = num % 400
            elif num >= 100: # C
                ans += 'C' * (num // 100)
                num = num % 100
            elif num >= 90: # XC
                ans += 'XC' * (num // 90)
                num = num % 90
            elif num >= 50: # L
                ans += 'L' * (num // 50)
                num = num % 50
            elif num >= 40: # XL
                ans += 'XL' * (num // 40)
                num = num % 40
            elif num >= 10: # X
                ans += 'X' * (num // 10)
                num = num % 10
            elif num >= 9: # IX
                ans += 'IX' * (num // 9)
                num = num % 9
            elif num >= 5: # V
                ans += 'V' * (num // 5)
                num = num % 5
            elif num >= 4: # IV
                ans += 'IV' * (num // 4)
                num = num % 4
            elif num >= 1: # I
                ans += 'I' * (num // 1)
                num = 0
        return ans
