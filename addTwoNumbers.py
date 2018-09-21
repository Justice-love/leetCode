# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        inc = False
        for  i in range(100):
            s = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            if s == 9 and inc:
                # result[i] = 0
                result.append(0)
                inc = True
            elif s == 9 and not inc:
                # result[i] = 9
                result.append(9)
                inc = False
            elif s > 9 and inc:
                # result[i] = (s / 10 ) + 1
                result.append(s - 10 + 1)
                inc = True
            elif s > 9 and not inc:
                # result[i] = s / 10
                result.append(s - 10)
                inc = True
            elif s < 9 and inc:
                # result[i] = s + 1;
                result.append(s + 1)
                inc = False
            else:
                # result[i] = s
                result.append(s)
                inc = False

            if l1 == None and l2 == None:
                if inc:
                    result.append(1)
                break
            if l1 == None and l2 :
                l1 = ListNode(0)
            if l1 and l2 == None:
                l2 = ListNode(0)



        return result




