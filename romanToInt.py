class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        temp = 0
        if re.search('CM', s):
            temp += 900
            s = re.sub('CM', '', s)
        if re.search('CD', s):
            temp += 400
            s = re.sub('CD', '', s)
        if re.search('XC', s):
            temp += 90
            s = re.sub('XC', '', s)
        if re.search('XL', s):
            temp += 40
            s = re.sub('XL', '', s)
        if re.search('IX', s):
            temp += 9
            s = re.sub('IX', '', s)
        if re.search('IV', s):
            temp += 4
            s = re.sub('IV', '', s)

        ro = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        for c in s:
            temp += ro[c]

        return temp


s = Solution()
print s.romanToInt('LVIII')