class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xStr = str(x)[::-1]
        f = False
        if '-' == xStr[len(xStr) - 1:]:
            xStr = xStr[:len(xStr) - 1]
            f = True
        xStr = self.d0(xStr)
        if f :
            xStr = '-' + xStr

        lv = long(xStr)
        if lv > 2147483647 and not f:
            return 0
        elif lv < -2147483648 and f:
            return 0
        else:
            return int(xStr)



    def d0(self, str):
        if len(str) == 1:
            return str
        elif str[0] == '0':
            return self.d0(str[1:])
        else:
            return str

s = Solution()
print  s.reverse(1534236469)
