class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                if c in stack:
                    del stack[:stack.index(c) + 1]
                    stack.append(c)
                else:
                    stack.append(c)

                if len(stack) > result:
                    result = len(stack)

        if len(stack) > result:
            return len(stack)
        else:
            return result



s = Solution()
print s.lengthOfLongestSubstring('cdd')