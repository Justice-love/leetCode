class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mylist = []
        if nums1 == None:
            nums1 = []
        if nums2 == None:
            nums2 = []
        mylist.extend(nums1)
        mylist.extend(nums2)

        myset = set(mylist)
        mylist = list(myset)
        mylist.sort()

        i = len(mylist) / 2
        print mylist
        print i
        if len(mylist) % 2 == 1:
            return mylist[i]
        else:
            return (mylist[i] - 1 + mylist[i]) / 2.0

s = Solution()
print s.findMedianSortedArrays([1, 1], [1, 2])


