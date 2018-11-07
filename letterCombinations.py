class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        resultL = []
        resultLT = []
        if digits == 0:
            return resultL


        d = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z']
        }

        for i in range(len(digits)):
            if len(resultL) == 0:
                resultL.extend(d[int(digits[i])])
                continue
            for j in range(len(resultL)):
                nl = d[int(digits[i])]
                for k in range(len(nl)):
                    resultLT.append(resultL[j] + nl[k])
            del resultL[:]
            resultL.extend(resultLT)
            del resultLT[:]

        return resultL


if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations('32')
