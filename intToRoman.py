class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = num / 1000
        last = num % 1000
        b = last / 500
        last = last % 500
        c = last / 100
        last = last % 100
        d = last / 50
        last %= 50
        e = last / 10
        last %= 10
        f = last / 5
        last %= 5
        g = last
        sign = [a, 0, b, 0, c, 0, d, 0, e, 0, f, 0, g]
        ro = {0:'M',1:'CM', 2:'D', 3:'CD', 4:'C', 5:'XC', 6:'L', 7:'XL', 8:'X', 9:'IX', 10:'V', 11:'IV', 12:'I'}
        for i in range(1, len(sign), 4):
            if sign[i+ 1] == 1 and sign[i + 3] == 4:
                sign[i] = 1
                sign[i + 1] = sign[i + 3] =0
            elif sign[i + 3] == 4:
                sign[i + 2] = 1
                sign[i + 3] = 0
        result = ''
        for i, n in enumerate(sign):
            result += n * ro[i]
        return result

s = Solution()
print s.intToRoman(3)
