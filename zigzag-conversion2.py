class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2
        result = ""

        if str_length == 0 or numRows == 0 or numRows == 1:
            return s

        for i in range(numRows):
            for j in range(i, str_length, node_length):
                result += s[j]
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]
        return result

