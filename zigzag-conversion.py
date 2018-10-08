class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print len(s)
        if numRows == 1:
            return s
        elif numRows == 2:
            return self.two(s, numRows)
        else:
            return self.mt(s, numRows)


    def two(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :return: str
        """
        rl = [[], []]
        for i, c in enumerate(s):
            rl[i %2].append(c)

        str = ''
        for rli in rl:
            for c in rli:
                str += c
        return str


    def mt(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :return: str
        """
        rl = [[] for i in range(numRows)]
        zn = numRows - 2
        zall = numRows + zn
        for i in range(len(s) / zall if len(s) % zall == 0 else len(s) / zall + 1) :
            for j in range(numRows - 1) :
                if j == 0:
                    for m in range(numRows) :
                        rl[m].append(1)
                else:
                    for k in range(numRows):
                        if numRows - j -1 == k:
                            rl[k].append(1)
                        else:
                            rl[k].append(0)

        l = numRows * len(rl[0])
        for c in s:
            for i in range(l):
                if rl[i % numRows][i / numRows] == 1:
                    rl[i % numRows][i / numRows] = c
                    break



        str = ''
        for rli in rl:
            for c in rli:
                if c != 0 and c != 1:
                    str += c

        return str



s = Solution()
print s.convert('gnvhcxwaqkxhazrpthjdlcmraadnnmiuaebe', 14)

