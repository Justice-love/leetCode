class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs.sort(lambda m1, m2: 1 if len(m1) > len(m2) else -1 )
        str1 = strs[0]
        if len(str1) == 0:
            return ''
        r = 0
        break_flag = False
        for i, s in enumerate(str1):
            for j in range(1, len(strs)):
                if strs[j][i] != s:
                    r = i - 1
                    break_flag = True
                    break

            if break_flag: break

        if not break_flag:
            r = i

        if r < 0:
            return ''
        else:
            return strs[0][0: r+1]

s = Solution()
print s.longestCommonPrefix([''])
