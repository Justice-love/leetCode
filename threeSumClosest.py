class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 4:
            return sum(nums)

        nums = sorted(nums)
        result = [2 ** 31 - 1, 0]

        for i in range(len(nums) - 1, -1, -1):
            remain = target - nums[i]
            if i < 2:
                break

            if remain > 0 and nums[0] > 0 and  nums[0] > remain:
                last = remain - nums[0] - nums[1]
                if result[0] > abs(last):
                    result = [abs(last), last]
                continue

            r, l = i - 1, 0
            while True:
                if r == l:
                    break
                temp = nums[l] + nums[r]
                last = remain - temp
                if last > 0:
                    l +=1
                    if result[0] > abs(last):
                        result = [abs(last), last]
                elif last < 0:
                    r -=1
                    if result[0] > abs(last):
                        result = [abs(last), last]
                else:
                    # some = 0
                    return target


        if result[1] < 0:
            return target + result[0]
        else:
            return target - result[0]



s = Solution()
# print s.threeSumClosest([0,-16,-11,-4,6,20,-17,10,14,-11,-16,17,-14,-11,8,-4,0,-2,10,15,0,-2,-3,19,17,-18,8,-16,-4,-16,-20,16,-16,5,-3,-18,-12,-18,-9,11,3,-14,-18,8,11,-9,-1,6,1,-17,-9,-7,11,-10,18,-1,4,-8,1,-20,-19,-19,12,13,14,15,0,18,3,8,-4,18,-1,6,-19,-11,11,14,12,11,-15,2,4,-1,5,3,-17,15,-1,-15,3,16,-11,-14,14,4,-7,-20,-2,-14,-8,-12,-12,18,4,-12,16], -31)
# print  s.threeSumClosest([1,1,1,1], 0)
print  s.threeSumClosest([89,-17,-41,9,56,-8,40,38,98,-31,80,-1,-40,-73,28,55,15,89,-83,87,-42,-22,61,64,-94,-33,-38,25,-20,-80,37,99,-72,74,16,-25,-21,-73,-73,-72,65,-4,-72,46,60,7,-25,-14,-58,-50,14,-99,88,50,75,-59,94,-74,25,23,-10,-47,-1,-30,81,-66,54,-64,-1,68,-1,47,55,-59,5,64,45,83,-3,-38,-59,46,33,54,55,9,-13,50,-43,-48,57,97,-55,-13,-25,-9,-20,63,30,88,-4,74,19,-87,-32], -297)