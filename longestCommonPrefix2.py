class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        print sorted(strs)
        print strs
        if not strs:
            return ''
        min_1=min(strs)
        max_1=max(strs)
        print min_1
        for i,value in enumerate(min_1):
            if value!=max_1[i]:
                return min_1[:i]
        return min_1

s = Solution()
print s.longestCommonPrefix(['za', 'zaaa', 'bbb'])