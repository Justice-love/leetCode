class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = []
        for s in str:
            result.append(s.lower())

        return ''.join(result)
