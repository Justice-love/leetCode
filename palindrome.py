class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        src = str(x)
        des = src[::-1]
        return src == des

