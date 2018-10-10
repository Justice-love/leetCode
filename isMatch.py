class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pa = re.compile('^' + p + '$')
        m = pa.match(s)
        return m != None and None != m.group(0)