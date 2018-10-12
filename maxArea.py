class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        for i, h in enumerate(height):
            for j in range(i + 1, len(height)):
                maxArea = max(maxArea, min(h , height[j]) * (j - i))

        return maxArea
