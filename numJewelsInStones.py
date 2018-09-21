class Solution(object):


    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict = {}
        for s in S:
            dictValueIncrease(dict, s)
        result = 0
        for j in J:
            if dict.has_key(j) :
                result = result + dict.get(j)

        return result

def dictValueIncrease( dict, key):
    if dict.has_key(key):
        dict[key] = dict.pop(key) +1
    else:
        dict[key] = 1

x = Solution()
x.numJewelsInStones('sstr' , 'ssrt')
