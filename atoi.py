class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        import re as st
        p = st.compile(r'^(?P<number>(\-|\+)?\d+)')
        m = p.search(str)
        if None == m:
            return 0
        sn = m.group('number')
        n = int(sn)
        if n < -2 ** 31:
            return -2 ** 31
        elif n > 2 ** 31 -1:
            return 2 ** 31 - 1
        else:
            return n




s = Solution()
print s.myAtoi(' -42')